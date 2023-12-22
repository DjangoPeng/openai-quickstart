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

            for pdf_page in pages_to_parse:
                page = Page()

                # Step 1: Extract all tables
                tables = pdf_page.extract_tables()

                # Step 2: Extract each line's content and characters' properties
                text_lines_info = pdf_page.extract_text_lines(layout=True, strip=True, return_chars=True)

                # Convert tables into a flat list for easier lookup
                flattened_tables_texts = [''.join([cell for row in table for cell in row]).replace(' ', '') for table in tables]

                table_coordinates = [None] * len(tables)
                table_font = [None] * len(tables)
                first_table_row_coordinates = [None] * len(tables)

                current_text = ""
                current_bbox = None
                current_font = None
                current_fontsize = None
                current_fontcolor = None

                for line_info in text_lines_info:
                    line_text = line_info['text']

                    # Check if the line corresponds to a table row
                    line_text_stripped = line_text.replace(' ', '')
                    table_index = next((i for i, table_text in enumerate(flattened_tables_texts) if line_text_stripped in table_text), None)

                    # Extract properties from the first character of the line
                    first_char_info = line_info['chars'][0]
                    char_font = first_char_info['fontname']
                    char_fontsize = first_char_info['size']
                    char_fontcolor = first_char_info['non_stroking_color']
                    char_bbox = (line_info['x0'], line_info['top'], line_info['x1'], line_info['bottom'])
                    if current_bbox is None:
                        current_bbox = char_bbox

                    if table_index is not None:
                        # If this is a table row
                        if first_table_row_coordinates[table_index] is None:
                            first_table_row_coordinates[table_index] = char_bbox
                        else:
                            table_coordinates[table_index] = (first_table_row_coordinates[table_index][0], first_table_row_coordinates[table_index][1], char_bbox[2], char_bbox[3])
                            table_font[table_index] = (char_font, char_fontsize, char_fontcolor)
                        continue
                    else:
                        # Regular text logic
                        if current_fontsize == char_fontsize:
                            current_text += "\n" + line_text
                            current_bbox = (current_bbox[0], current_bbox[1], char_bbox[2], char_bbox[3])
                        else:
                            if current_text:
                                text_content = Content(
                                    content_type=ContentType.TEXT,
                                    original=current_text,
                                    coordinates=current_bbox,
                                    font=current_font,
                                    fontsize=current_fontsize,
                                    fontcolor=current_fontcolor
                                )
                                page.add_content(text_content)

                            current_text = line_text
                            current_bbox = char_bbox
                            current_font = char_font
                            current_fontsize = char_fontsize
                            current_fontcolor = char_fontcolor

                # Save any remaining content
                if current_text:
                    text_content = Content(
                        content_type=ContentType.TEXT,
                        original=current_text,
                        coordinates=current_bbox,
                        font=current_font,
                        fontsize=current_fontsize,
                        fontcolor=current_fontcolor
                    )
                    page.add_content(text_content)

                # Step 4: Add tables as content
                for i, table_data in enumerate(tables):
                    table_content = TableContent(data=table_data)
                    if table_coordinates[i]:
                        table_content.coordinates = table_coordinates[i]
                    if table_font[i]:
                        table_content.font, table_content.fontsize, table_content.fontcolor = table_font[i]
                    page.add_content(table_content)

                # Add image support
                image_directory = os.path.dirname(pdf_file_path)
                for idx, img_meta in enumerate(pdf_page.images):
                    # Extract image with bounding box using cropping
                    image_bbox = (img_meta['x0'], img_meta['top'], img_meta['x1'], img_meta['bottom'])
                    cropped = pdf_page.crop(image_bbox)
                    
                    # Convert cropped region to image
                    img = cropped.to_image(antialias=True)
    
                    # Save the image with a specific naming convention: page number and image index
                    image_file_path = os.path.join(image_directory, f"page_{pdf_page.page_number}_img_{idx}.png")
                    img.save(image_file_path, format="PNG")
    
                    # Create an ImageContent instance and add it to the page
                    image_content = ImageContent(coordinates=image_bbox, imagepath=image_file_path)
                    page.add_content(image_content)

                # Extract lines from the PDF page and add them as LineContent
                for line in pdf_page.lines:
                    x1, y1, x2, y2 = line['x0'], line['top'], line['x1'], line['bottom']
                    line_width = line['width']
                    line_color = line['non_stroking_color']
                    line_content = LineContent((x1, y1, x2, y2), line_width, line_color)
                    page.add_content(line_content)

                # save layout
                page.sort_contents()

                book.add_page(page)

        return book