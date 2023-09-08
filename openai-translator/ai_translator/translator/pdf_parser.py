# 导入 pdfplumber 库，用于解析 PDF 文件
import pdfplumber
# 导入 Optional 类型，用于指定可选参数的类型
from typing import Optional
# 导入 Book、Page、Content、ContentType 和 TableContent 类，用于表示书籍、页面、内容、内容类型和表格内容
from book import Book, Page, Content, ContentType, TableContent
# 导入 PageOutOfRangeException 异常，用于表示页面超出范围的错误
from translator.exceptions import PageOutOfRangeException
# 导入 LOG 对象，用于记录日志
from utils import LOG

class PDFParser:
    def __init__(self):
        pass

    # 解析 PDF 文件，返回 Book 对象
    # 第一个参数 pdf_file_path 用于指定要解析的 PDF 文件的路径
    # 第二个参数 pages 用于指定解析的页数，如果不指定，则解析所有页，如果指定了页数，但页数超出了 PDF 文件的总页数，则抛出异常
    def parse_pdf(self, pdf_file_path: str, pages: Optional[int] = None) -> Book:
        # 创建一个Book对象，用于存储解析后的PDF内容
        book = Book(pdf_file_path)

        # 打开PDF文件
        with pdfplumber.open(pdf_file_path) as pdf:
            # 如果指定了页数，但页数超出了PDF文件的总页数，则抛出异常
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)

            # 如果没有指定页数，则解析所有页
            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            # 遍历每一页
            for pdf_page in pages_to_parse:
                # 创建一个Page对象，用于存储解析后的PDF页面内容
                page = Page()

                # 提取原始文本内容和表格数据
                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()

                # 从原始文本中移除表格中的每个单元格的内容
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            # 如果单元格的内容不为空，则从原始文本中移除单元格的内容
                            raw_text = raw_text.replace(cell, "", 1)

                # 处理文本内容
                if raw_text:
                    # 移除空行和前导/尾随空格
                    # 1. 使用splitlines()方法将原始文本按行分割，返回一个列表
                    raw_text_lines = raw_text.splitlines()
                    # 2. 使用strip()方法移除每一行的前导/尾随空格
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    # 3. 使用join()方法将列表中的每一行连接起来，返回一个字符串
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines)

                    # 创建一个Content对象，用于存储文本内容
                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)
                    LOG.debug(f"[raw_text]\n {cleaned_raw_text}")

                # 处理表格内容
                if tables:
                    # 创建一个TableContent对象，用于存储表格内容
                    table = TableContent(tables)
                    page.add_content(table)
                    LOG.debug(f"[table]\n{table}")

                # 将解析后的页面内容添加到Book对象中
                book.add_page(page)

        # 返回解析后的Book对象
        return book