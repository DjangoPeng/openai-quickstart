import pdfplumber  # 导入pdfplumber库，用于解析PDF文件
from typing import Optional  # 导入typing库中的Optional类型，用于指定可选参数
from book import Book, Page, Content, ContentType, TableContent  # 导入自定义的Book、Page、Content、ContentType和TableContent类
from translator.exceptions import PageOutOfRangeException  # 导入自定义的PageOutOfRangeException异常类
from utils import LOG  # 导入自定义的LOG函数，用于记录日志

# 创建一个PDFParser类，用于解析PDF文件
class PDFParser:
    def __init__(self):
        pass

    # 解析PDF文件，返回一个Book对象
    # pdf_file_path: PDF文件的路径
    # pages: 解析的页数，如果不指定，则解析所有页
    def parse_pdf(self, pdf_file_path: str, pages: Optional[int] = None) -> Book:
        # 创建一个Book对象，用于存储解析后的PDF内容
        book = Book(pdf_file_path)

        # 打开PDF文件
        with pdfplumber.open(pdf_file_path) as pdf:
            # 如果指定了解析页数，但页数超出了PDF文件的总页数，则抛出异常
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)

            # 如果没有指定解析页数，则解析所有页
            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            # 遍历每一页
            for pdf_page in pages_to_parse:
                # 创建一个Page对象，用于存储当前页的内容
                page = Page()

                # 获取当前页的原始文本内容和表格内容
                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()

                # 从原始文本中移除表格中的每个单元格的内容
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            raw_text = raw_text.replace(cell, "", 1)

                # 处理文本内容
                if raw_text:
                    # 将原始文本按行分割
                    raw_text_lines = raw_text.splitlines()
                    # 将每一行的前后空格移除
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    # 将每一行的内容拼接起来
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

                # 将当前页的内容添加到Book对象中
                book.add_page(page)

        # 返回解析后的Book对象
        return book