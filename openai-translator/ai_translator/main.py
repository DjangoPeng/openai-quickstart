import sys  # 导入 sys 模块，用于添加系统路径
import os  # 导入 os 模块，用于访问操作系统功能

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前文件所在目录添加到系统路径中，以便导入其他模块

from utils import ArgumentParser, ConfigLoader, LOG  # 导入自定义模块 utils 中的 ArgumentParser、ConfigLoader 和 LOG 类
from model import GLMModel, OpenAIModel  # 导入自定义模块 model 中的 GLMModel 和 OpenAIModel 类
from translator import PDFTranslator  # 导入自定义模块 translator 中的 PDFTranslator 类

if __name__ == "__main__":
    argument_parser = ArgumentParser()  # 实例化 ArgumentParser 类
    args = argument_parser.parse_arguments()  # 解析命令行参数

    config_loader = ConfigLoader(args.config)  # 实例化 ConfigLoader 类，并传入配置文件路径
    config = config_loader.load_config()  # 加载配置文件

    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']  # 获取 OpenAI 模型名称
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']  # 获取 OpenAI API 密钥
    model = OpenAIModel(model=model_name, api_key=api_key)  # 实例化 OpenAIModel 类，并传入模型名称和 API 密钥

    pdf_file_path = args.book if args.book else config['common']['book']  # 获取 PDF 文件路径
    file_format = args.file_format if args.file_format else config['common']['file_format']  # 获取文件格式

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)