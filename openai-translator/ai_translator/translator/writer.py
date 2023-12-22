import os
from reportlab.lib import colors, pagesizes, units
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
)
from reportlab.platypus.flowables import Flowable
from book import Book, ContentType
from utils import LOG

class LineFlowable(Flowable):
    """ Custom flowable to draw a line. """
    
    def __init__(self, x1, x2, width, color):
        Flowable.__init__(self)
        self.x1 = x1
        self.x2 = x2
        self.width = width
        self.color = color

    def draw(self):
        # Get the current canvas.
        canvas = self.canv
        y = self.canv._y  # Current y-position in the canvas

        canvas.setStrokeColor(self.color)
        canvas.setLineWidth(self.width)
        canvas.line(self.x1, y, self.x2, y)

class Writer:
    def __init__(self):
        pass

    def save_translated_book(self, book: Book, output_file_path: str = None, file_format: str = "PDF"):
        if file_format.lower() == "pdf":
            self._save_translated_book_pdf(book, output_file_path)
        elif file_format.lower() == "markdown":
            self._save_translated_book_markdown(book, output_file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    def _save_translated_book_pdf(self, book: Book, output_file_path: str = None):
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.pdf')

        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")

        # Register Chinese font
        font_path = "../fonts/simsun.ttc"  # 请将此路径替换为您的字体文件路径
        pdfmetrics.registerFont(TTFont("SimSun", font_path))

        # Create a PDF document
        doc = SimpleDocTemplate(output_file_path, pagesize=pagesizes.letter)
        styles = getSampleStyleSheet()
        story = []

        # Iterate over the pages and contents
        for page in book.pages:
            for content in page.contents:
                if content.status:
                    match content.content_type:
                        case ContentType.TEXT:
                            # Add translated text to the PDF
                            text = content.translation
                            simsun_style = ParagraphStyle('SimSun', fontName='SimSun', 
                                                          fontSize=round(content.fontsize), 
                                                          leading=round(content.fontsize * 1.2))
                            para = Paragraph(text, simsun_style)
                            story.append(para)
    
                        case ContentType.TABLE:
                            # Add table to the PDF
                            table = content.translation
                            table_style = TableStyle([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),  # 更改表头字体为 "SimSun"
                                ('FONTSIZE', (0, 0), (-1, 0), round(content.fontsize)),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), round(content.fontsize)),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),  # 更改表格中的字体为 "SimSun"
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)
                            ])
                            pdf_table = Table(table.values.tolist())
                            pdf_table.setStyle(table_style)
                            story.append(pdf_table)
                            
                        case ContentType.IMAGE:
                            img = Image(content.imagepath)
                            story.append(img)
                            
                        case ContentType.LINE:
                            line = LineFlowable(content.coordinates[0], content.coordinates[2],
                                                content.line_width, content.line_color)
                            story.append(line)
                        case _:
                            pass
                        
            # Add a page break after each page except the last one
            if page != book.pages[-1]:
                story.append(PageBreak())

        # Save the translated book as a new PDF file
        doc.build(story)
        LOG.info(f"翻译完成: {output_file_path}")
        
    def _save_translated_book_markdown(self, book: Book, output_file_path: str = None):
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.md')

        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Iterate over the pages and contents
            for page in book.pages:
                for content in page.contents:
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            # Add translated text to the Markdown file
                            text = content.translation
                            output_file.write(text + '\n\n')

                        elif content.content_type == ContentType.TABLE:
                            # Add table to the Markdown file
                            table = content.translation
                            header = '| ' + ' | '.join(str(column) for column in table.columns) + ' |' + '\n'
                            separator = '| ' + ' | '.join(['---'] * len(table.columns)) + ' |' + '\n'
                            # body = '\n'.join(['| ' + ' | '.join(row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            output_file.write(header + separator + body)

                # Add a page break (horizontal rule) after each page except the last one
                if page != book.pages[-1]:
                    output_file.write('---\n\n')

        LOG.info(f"翻译完成: {output_file_path}")