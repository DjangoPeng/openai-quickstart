import sys
import os
from argparse import Namespace

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

if __name__ == "__main__":
    #argument_parser = ArgumentParser()
    #args = argument_parser.parse_arguments()

    args = Namespace(config='config.yaml', model_type='OpenAIModel', glm_model_url=None, timeout=None,
              openai_model='gpt-3.5-turbo', openai_api_key=None, book='tests/test.pdf', file_format='markdown', pre_name_write='tests/img/', pre_name_read='img/')
    print(f"args = {args}")
    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()

    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    model = OpenAIModel(model=model_name, api_key=api_key)


    pdf_file_path = args.book if args.book else config['common']['book']
    file_format = args.file_format if args.file_format else config['common']['file_format']

    pre_name_write = args.pre_name_write if args.pre_name_write else config['common']['pre_name_write']
    pre_name_read = args.pre_name_read if args.pre_name_read else config['common']['pre_name_read']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, pre_name_write, pre_name_read, file_format)
