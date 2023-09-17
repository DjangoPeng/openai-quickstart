import pdfplumber
from typing import Optional
from book import Book, Page, Content, ContentType, TableContent
from translator.exceptions import PageOutOfRangeException
from utils import LOG


class PDFParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_file_path: str, pages: Optional[int] = None) -> Book:
        book = Book(pdf_file_path)

        with pdfplumber.open(pdf_file_path) as pdf:
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)

            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]
            img_num = 1
            for pdf_page in pages_to_parse:
                page = Page()

                # Store the original text content
                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()
                images_in_page = pdf_page.images

                # Remove each cell's content from the original text
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            raw_text = raw_text.replace(cell, "", 1)

                # Handling text
                if raw_text:
                    # Remove empty lines and leading/trailing whitespaces
                    raw_text_lines = raw_text.splitlines()
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines)

                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)
                    LOG.debug(f"[raw_text]\n {cleaned_raw_text}")



                # Handling tables
                if tables:
                    table = TableContent(tables)
                    page.add_content(table)
                    LOG.debug(f"[table]\n{table}")
                    
           
                if images_in_page:
                    page_height = pdf_page.height
                    for image in images_in_page:
                        image_bbox = (image['x0'], page_height - image['y1'], image['x1'], page_height - image['y0'])
                        cropped_page = pdf_page.crop(image_bbox)
                        image_obj = cropped_page.to_image(resolution=200)
                        #img_name = (pdf_file_path.replace('test.pdf', f'images/'))+str(img_num)+".jpg"
                        img_name = (pdf_file_path.replace('test.pdf', ''))+str(img_num)+".jpg"
                        #image_obj.save("tests/1.jpg")
                        image_obj.save(img_name)
                        page.contents.append(img_name)
                        img_num+=1
                book.add_page(page)

        return book
