from typing import Optional
from ai_translator.model import Model
from ai_translator.translator.pdf_parser import PDFParser
from ai_translator.translator.writer import Writer
from ai_translator.utils import LOG

from ai_translator.book import ContentType


class PDFTranslator:
    language = {
        "English": "英文",
        "中文": "中文",
        "にほんご": "日语"
    }

    def __init__(self, model: Model):
        self.model = model
        self.pdf_parser = PDFParser()
        self.writer = Writer()

    def translate_pdf(self, pdf_file_path: str, file_format: str = 'PDF', target_language: str = '中文', output_file_path: str = None, pages: Optional[int] = None):
        self.book = self.pdf_parser.parse_pdf(pdf_file_path, pages)
        target_language = self.language.get(target_language)

        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                prompt = self.model.translate_prompt(content, target_language)
                LOG.debug(prompt)

                # 调试用，不调用API
                # translation = content.original
                # status = True
                # if content.content_type == ContentType.TEXT:
                #     translation = PDFTranslator.TEXT_TRASACTION_RESULT
                # elif content.content_type == ContentType.TABLE:
                #     translation = PDFTranslator.TABLE_TRASACTION_RESULT

                translation, status = self.model.make_request(prompt)
                LOG.info(translation)
                
                # Update the content in self.book.pages directly
                self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)

        return self.writer.save_translated_book(self.book, output_file_path, file_format)

    TABLE_TRASACTION_RESULT = "[水果, 颜色, 价格（美元）]\n" + \
                    "[苹果, 红色, 1.20]\n" + \
                    "[香蕉, 黄色, 0.50]\n" + \
                    "[橙子, 橙色, 0.80]\n" + \
                    "[草莓, 红色, 2.50]\n" + \
                    "[蓝莓, 蓝色, 3.00]\n" + \
                    "[奇异果, 绿色, 1.00]\n" + \
                    "[芒果, 橙色, 1.50]\n" + \
                    "[葡萄, 紫色, 2.00]"
    TEXT_TRASACTION_RESULT = "测试数据\n" + \
                    "这个数据集包含了由OpenAI的AI语言模型ChatGPT提供的两个测试样本。\n" + \
                    "这些样本包括一个Markdown表格和一段英文文本，可以用来测试支持文本和表格格式的英译中翻译软件。\n" + \
                    "文本测试\n" + \
                    "敏捷的棕色狐狸跳过懒惰的狗。这个句子包含了英文字母表中的每个字母至少一次。句子是常用来测试字体、键盘和其他与文本相关的工具的。除了英语，还有许多其他语言中的句子。由于语言的独特特性，有些句子更难构建。\n" + \
                    "表测试\n"