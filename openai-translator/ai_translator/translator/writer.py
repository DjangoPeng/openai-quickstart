# 导入 os 模块，用于访问操作系统功能
import os
# 导入 reportlab 库中的 colors、pagesizes、units 模块，用于设置 PDF 文件的颜色、页面大小、单位等
from reportlab.lib import colors, pagesizes, units
# 导入 reportlab 库中的 getSampleStyleSheet、ParagraphStyle 模块，用于设置 PDF 文件中的样式
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# 导入 reportlab 库中的 pdfmetrics、TTFont 模块，用于设置 PDF 文件中的字体
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# 导入 reportlab 库中的 SimpleDocTemplate、Paragraph、Spacer、Table、TableStyle、PageBreak 模块，用于创建 PDF 文件的各种元素
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
# 导入自定义的 Book、ContentType 类，用于表示书籍和内容类型
from book import Book, ContentType
# 导入自定义的 LOG 函数，用于记录日志
from utils import LOG

class Writer:
    def __init__(self):
        pass

    # 保存翻译后的书籍
    # 第一个参数 book 是 Book 类的实例
    # 第二个参数 output_file_path 是输出文件的路径
    # 第三个参数 file_format 是输出文件的格式,支持 PDF 和 Markdown
    def save_translated_book(self, book: Book, output_file_path: str = None, file_format: str = "PDF"):
        # 判断输出文件的格式,支持PDF和Markdown
        if file_format.lower() == "pdf":
            self._save_translated_book_pdf(book, output_file_path) 
        elif file_format.lower() == "markdown":
            self._save_translated_book_markdown(book, output_file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    def _save_translated_book_pdf(self, book: Book, output_file_path: str = None):
        # 如果未指定输出路径,则使用默认路径
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.pdf')

        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")
        
        # 注册中文字体
        font_path = "../fonts/simsun.ttc"  # 请将此路径替换为您的字体文件路径
        pdfmetrics.registerFont(TTFont("SimSun", font_path))
        
        # 创建使用SimSun字体的ParagraphStyle
        simsun_style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12, leading=14)
        
        # 创建PDF文档
        # 页面大小为A4纸张大小
        doc = SimpleDocTemplate(output_file_path, pagesize=pagesizes.letter)
        # 设置页面的左、右、上、下边距
        styles = getSampleStyleSheet()
        # 创建一个空的列表,用于存储PDF中的元素
        story = []
        
        # 遍历页面和内容
        for page in book.pages:
            for content in page.contents:
                # 如果内容已翻译
                if content.status:
                    if content.content_type == ContentType.TEXT:
                        # 将翻译后的文本添加到PDF中  
                        text = content.translation
                        para = Paragraph(text, simsun_style)
                        story.append(para)
                        
                    elif content.content_type == ContentType.TABLE:
                        # 将表格添加到PDF中
                        table = content.translation
                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey), # 设置表头背景颜色
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), # 设置表头文本颜色
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # 设置表格中的文本对齐方式
                            ('FONTNAME', (0, 0), (-1, 0), 'SimSun'), # 设置表头字体
                            ('FONTSIZE', (0, 0), (-1, 0), 14), # 设置表头字体大小
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12), # 设置表头下边距
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige), # 设置表格内容背景颜色
                            ('FONTNAME', (0, 1), (-1, -1), 'SimSun'), # 设置表格内容字体
                            ('GRID', (0, 0), (-1, -1), 1, colors.black) # 设置表格框线
                        ])
                        pdf_table = Table(table.values.tolist())
                        pdf_table.setStyle(table_style)
                        story.append(pdf_table)
                        
            # 在每页之后添加分页符,最后一页除外
            if page != book.pages[-1]:
                story.append(PageBreak())
                
        # 将翻译后的书保存为新的PDF文件  
        doc.build(story)
        LOG.info(f"翻译完成: {output_file_path}")

    def _save_translated_book_markdown(self, book: Book, output_file_path: str = None):
        # 如果未指定输出路径,则使用默认路径 
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.md')

        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")
        # 打开文件,并设置编码为utf-8
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # 遍历页面和内容
            for page in book.pages:
                for content in page.contents:
                    # 如果内容已翻译
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            # 将翻译后的文本添加到Markdown文件中
                            text = content.translation
                            output_file.write(text + '\n\n')
                            
                        elif content.content_type == ContentType.TABLE:
                            # 将表格添加到Markdown文件中
                            table = content.translation
                            header = '| ' + ' | '.join(str(column) for column in table.columns) + ' |' + '\n'
                            separator = '| ' + ' | '.join(['---'] * len(table.columns)) + ' |' + '\n'
                            # body = '\n'.join(['| ' + ' | '.join(row) for row in table.values.tolist()]) + '\n\n'
                            body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            output_file.write(header + separator + body)
                            
                # 在每页之后添加分隔符(水平线),最后一页除外
                if page != book.pages[-1]:
                    output_file.write('---\n\n')
                    
        LOG.info(f"翻译完成: {output_file_path}")