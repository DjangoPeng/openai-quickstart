import os  # 导入操作系统模块，用于获取文件路径
from reportlab.lib import colors, pagesizes, units  # 导入 reportlab 库中的颜色、页面大小和单位模块，用于设置 PDF 页面
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # 导入 reportlab 库中的样式模块，用于设置 PDF 文本样式
from reportlab.pdfbase import pdfmetrics  # 导入 reportlab 库中的 pdfmetrics 模块，用于配置字体
from reportlab.pdfbase.ttfonts import TTFont  # 导入 reportlab 库中的 TTFont 模块，用于配置字体
# 导入 reportlab 库中的 SimpleDocTemplate、Paragraph、Spacer、Table、TableStyle 和 PageBreak 类，用于创建 PDF 文档
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

from book import Book, ContentType  # 导入自定义的 Book 和 ContentType 类，用于获取翻译后的内容
from utils import LOG  # 导入自定义的 LOG 函数，用于打印日志

# Writer 类,用于将翻译后的内容保存为指定格式的文件
class Writer:
    def __init__(self):
        pass
		
    # 将翻译后的书籍内容保存为指定格式的文件
    # book: Book 类型,翻译后的书籍内容
    # book.pdf_file_path: str 类型,翻译前的PDF文件路径
    # ouput_file_format: str 类型,输出文件格式,支持PDF和Markdown
    def save_translated_book(self, book: Book, ouput_file_format: str): 
        # 打印输出文件格式
        LOG.debug(ouput_file_format)  

        # 根据输出文件格式,保存为PDF或Markdown
        if ouput_file_format.lower() == "pdf":
            output_file_path = self._save_translated_book_pdf(book)
        elif ouput_file_format.lower() == "markdown":
            output_file_path = self._save_translated_book_markdown(book)
        else:
            # 不支持的文件格式,打印错误提示
            LOG.error(f"不支持文件类型: {ouput_file_format}")
            return ""

        # 打印已保存文件的路径    
        LOG.info(f"翻译完成,文件保存至: {output_file_path}") 

        return output_file_path


    # 将翻译内容保存为PDF文件
    def _save_translated_book_pdf(self, book: Book, output_file_path: str = None):
        
        # 构建PDF输出文件的路径 
        output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.pdf')  

        # 打印PDF输出文件路径
        LOG.info(f"开始导出: {output_file_path}")

        # 注册中文字体
        font_path = "../fonts/simsun.ttc"  # 请将此路径替换为您的字体文件路径
        pdfmetrics.registerFont(TTFont("SimSun", font_path))

        # 创建使用SimSun字体的Paragraph样式
        simsun_style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12, leading=14)
        
        # 创建PDF文档对象，设置页面大小为A4
        doc = SimpleDocTemplate(output_file_path, pagesize=pagesizes.letter)
        # 设置PDF文档的左、右、上、下边距
        styles = getSampleStyleSheet()
        # 创建存储所有页面内容的列表
        story = []

        # 遍历所有页面内容
        for page in book.pages:
            for content in page.contents:
                # 如果翻译成功
                if content.status:
                    if content.content_type == ContentType.TEXT:
                        # 添加翻译后的文本内容
                        text = content.translation  
                        para = Paragraph(text, simsun_style)
                        story.append(para)

                    elif content.content_type == ContentType.TABLE:
                        # 添加表格内容
                        table = content.translation
                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey), # 设置表头背景颜色为灰色
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), # 设置表头文本颜色为白色
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # 设置表格中的文本对齐方式为居中
                            ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),  # 更改表头字体为 "SimSun"
                            ('FONTSIZE', (0, 0), (-1, 0), 14), # 更改表头字体大小为 14
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12), # 设置表头下边距为 12
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige), # 设置表格内容背景颜色为米色
                            ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),  # 更改表格中的字体为 "SimSun" 
                            ('GRID', (0, 0), (-1, -1), 1, colors.black) # 设置表格边框为黑色
                        ])
                        pdf_table = Table(table.values.tolist())
                        pdf_table.setStyle(table_style)
                        story.append(pdf_table)
            # 在每页之后插入分页符,最后一页除外
            if page != book.pages[-1]:
                story.append(PageBreak())

        # 生成并保存翻译后的PDF文件 
        doc.build(story)
        return output_file_path


    # 将翻译内容保存为Markdown文件
    def _save_translated_book_markdown(self, book: Book, output_file_path: str = None):
        # 构建Markdown输出文件的路径
        output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.md') 

        # 打印Markdown输出文件路径
        LOG.info(f"开始导出: {output_file_path}")
        # 打开Markdown输出文件
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # 遍历所有页面内容
            for page in book.pages:
                for content in page.contents:
                    # 如果翻译成功
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            # 添加翻译后的文本内容
                            text = content.translation
                            output_file.write(text + '\n\n')

                        elif content.content_type == ContentType.TABLE:
                            # 添加表格内容
                            table = content.translation
                            # 生成Markdown表格
                            header = '| ' + ' | '.join(str(column) for column in table.columns) + ' |' + '\n'
                            separator = '| ' + ' | '.join(['---'] * len(table.columns)) + ' |' + '\n'
                            # body = '\n'.join(['| ' + ' | '.join(row) for row in table.values.tolist()]) + '\n\n'
                            body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            output_file.write(header + separator + body)

                # 在每页之后插入分隔线,最后一页除外
                if page != book.pages[-1]:
                    output_file.write('---\n\n')

        return output_file_path