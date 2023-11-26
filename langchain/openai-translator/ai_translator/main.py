import sys  # 导入 sys 模块，用于添加系统路径
import os  # 导入 os 模块，用于获取文件路径

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前文件所在目录添加到系统路径中，以便导入其他模块

from utils import ArgumentParser, LOG  # 导入 utils 模块中的 ArgumentParser 和 LOG 类，用于解析命令行参数和打印日志
from translator import PDFTranslator, TranslationConfig  # 导入 translator 模块中的 PDFTranslator 和 TranslationConfig 类，用于翻译 PDF 文件

if __name__ == "__main__":
    # 解析命令行参数
    argument_parser = ArgumentParser()  # 创建 ArgumentParser 实例
    args = argument_parser.parse_arguments()  # 解析命令行参数

    # 设置 OpenAI API Key
    os.environ["OPENAI_API_KEY"] = args.api_key

    # 初始化配置
    config = TranslationConfig() 
    config.initialize(args)

    # 创建 PDFTranslator 实例
    translator = PDFTranslator(config.model_name)
    # 调用 translate_pdf() 方法进行 PDF 翻译
    translator.translate_pdf(config.input_file, config.output_file_format, pages=None)