from typing import Optional  # 引入 Optional 类型，表示可选参数
from translator.pdf_parser import PDFParser  # 引入 PDFParser 类，用于解析 PDF 文件
from translator.writer import Writer  # 引入 Writer 类，用于将翻译结果写入文件
from translator.translation_chain import TranslationChain  # 引入 TranslationChain 类，用于构建翻译链
from utils import LOG  # 引入 LOG 对象，用于记录日志

# PDFTranslator 类,用于将 PDF 文件翻译为指定格式的文件
class PDFTranslator:
    # 初始化 PDFTranslator 类，传入模型名称
    def __init__(self, model_name: str):
        # 初始化翻译链
        self.translate_chain = TranslationChain(model_name)
        # 初始化 PDF 解析器
        self.pdf_parser = PDFParser()
        # 初始化写入器
        self.writer = Writer()

    # 将 PDF 文件翻译为指定格式的文件
    # input_file: str 类型,输入文件路径
    # output_file_format: str 类型,输出文件格式,支持PDF和Markdown
    # source_language: str 类型,源语言,默认为英语
    # target_language: str 类型,目标语言,默认为中文
    # pages: Optional[int] 类型,翻译的页数,默认为 None,表示翻译所有页
    def translate_pdf(self,
                    input_file: str,
                    output_file_format: str = 'markdown',
                    source_language: str = "English",
                    target_language: str = 'Chinese',
                    pages: Optional[int] = None):
        # 解析 PDF 文件
        self.book = self.pdf_parser.parse_pdf(input_file, pages)

        # 遍历所有页面内容
        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                # 翻译每个页面的每个内容
                translation, status = self.translate_chain.run(content, source_language, target_language)
                # 保存翻译结果
                self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)
        
        # 保存翻译后的内容为指定格式的文件
        return self.writer.save_translated_book(self.book, output_file_format)