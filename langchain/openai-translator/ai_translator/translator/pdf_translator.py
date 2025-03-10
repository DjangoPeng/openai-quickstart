from typing import Optional
from translator.pdf_parser import PDFParser
from translator.writer import Writer
from translator.translation_chain import TranslationChain
from utils import LOG

class PDFTranslator:
    def __init__(self, model_name: str):
        self.translate_chain = TranslationChain(model_name)
        self.pdf_parser = PDFParser()
        self.writer = Writer()

    def translate_pdf(self,
                    input_file: str,
                    output_file_format: str = 'markdown',
                    source_language: str = "English",
                    target_language: str = 'Chinese',
                    style: str = 'none',
                    writer: str = 'none',
                    pages: Optional[int] = None):
        
        self.book = self.pdf_parser.parse_pdf(input_file, pages)

        style_template = f""
        if style != 'none':
            style_template += f"The translation is in {style} style."
        if writer != 'none':
            style_template += f"Refer to the style of writer {writer}"

        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                # Translate content.original
                translation, status = self.translate_chain.run(content, source_language, target_language,style_template)
                # Update the content in self.book.pages directly
                self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)
        
        return self.writer.save_translated_book(self.book, output_file_format)
