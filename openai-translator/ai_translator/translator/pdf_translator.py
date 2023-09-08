# 导入 typing 模块中的 Optional 类型
from typing import Optional
# 导入 Model 类，用于翻译模型的加载和使用
from model import Model
# 导入 PDFParser 类，用于解析 PDF 文件
from translator.pdf_parser import PDFParser
# 导入 Writer 类，用于将翻译结果写入文件
from translator.writer import Writer
# 导入 LOG 函数，用于记录日志
from utils import LOG

# PDFTranslator 类
class PDFTranslator:
    # 构造函数，接收一个 Model 类型的参数
    def __init__(self, model: Model):
        # 将传入的 Model 对象赋值给 self.model
        self.model = model
        # 创建 PDFParser 对象并赋值给 self.pdf_parser
        self.pdf_parser = PDFParser()
        # 创建 Writer 对象并赋值给 self.writer
        self.writer = Writer()

    # 翻译 PDF 文件
    # 第一个参数 pdf_file_path 用于指定要翻译的 PDF 文件的路径
    # 第二个参数 file_format 用于指定翻译后的文件格式，默认为 PDF
    # 第三个参数 target_language 用于指定目标语言，默认为中文
    # 第四个参数 output_file_path 用于指定翻译后的文件的保存路径，默认为 None，表示不保存
    # 第五个参数 pages 用于指定翻译的页数，默认为 None，表示翻译所有页
    def translate_pdf(self, pdf_file_path: str, file_format: str = 'PDF', target_language: str = '中文', output_file_path: str = None, pages: Optional[int] = None):
        # 解析 PDF 文件并返回一个 Book 对象，赋值给 self.book
        self.book = self.pdf_parser.parse_pdf(pdf_file_path, pages)

        # 遍历每一页和每个内容块
        for page_idx, page in enumerate(self.book.pages):
            for content_idx, content in enumerate(page.contents):
                # 将内容块传入 Model 对象的 translate_prompt 方法中，返回翻译的提示语句
                prompt = self.model.translate_prompt(content, target_language)
                # 打印提示语句
                LOG.debug(prompt)
                # 将提示语句传入 Model 对象的 make_request 方法中，返回翻译结果和状态
                translation, status = self.model.make_request(prompt)
                # 打印翻译结果
                LOG.info(translation)
                
                # 直接在 self.book.pages 中更新内容块的翻译结果和状态
                self.book.pages[page_idx].contents[content_idx].set_translation(translation, status)

        # 将翻译后的 Book 对象保存到文件中
        self.writer.save_translated_book(self.book, output_file_path, file_format)