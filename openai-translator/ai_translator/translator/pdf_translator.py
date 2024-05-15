from typing import Optional
from model import Model
from translator.pdf_parser import PDFParser
from translator.writer import Writer
from utils import LOG
from book import ContentType


class PDFTranslator:
    def __init__(self, model: Model):
        self.model = model
        self.pdf_parser = PDFParser()
        self.writer = Writer()

    def translate_pdf(self, pdf_file_path: str, pre_name_write: str, pre_name_read: str,file_format: str = 'PDF',target_language: str = '中文', output_file_path: str = None, pages: Optional[int] = None):
        self.book = self.pdf_parser.parse_pdf(pdf_file_path, pre_name_write, pages)

        LOG.debug(self.book.pages)
        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                if content.content_type != ContentType.IMAGE:
                    prompt = self.model.translate_prompt(content, target_language)
                    LOG.debug(prompt)
                    translation, status = self.model.make_request(prompt)
                    LOG.info(translation)

                    # Update the content in self.book.pages directly
                    self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)
                elif content.content_type == ContentType.IMAGE:
                    translation, status = content.translation, True
                    self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)
                


        output_file_path = self.writer.save_translated_book(self.book, pre_name_read, output_file_path, file_format)
        return output_file_path

    def translate_to_text(self, source_text: str, target_language: str) -> str:
        prompt = self.model.translate_prompt(source_text, target_language)
        LOG.debug(prompt)
        translation, status = self.model.make_request(prompt)
        return translation
