import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

OPENAI_MODEL_TYPE = 'OpenAIModel'
OPENAI_MODEL_REQUIRED_MESSAGE = 'openai_model and openai_api_key are required when using OpenAIModel'
OTHER_MODEL_MESSAGE = 'other model will be supported later ...'

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    config_loader = ConfigLoader(args.config)
    config = config_loader.load_config()

    model_config = config.get(OPENAI_MODEL_TYPE, {})
    model_name = args.openai_model or model_config.get('model')
    api_key = args.openai_api_key or model_config.get('api_key')

    if args.model_type == OPENAI_MODEL_TYPE:
        if model_name and api_key:
            model = OpenAIModel(model=model_name, api_key=api_key)
            pdf_file_path = args.book if args.book else config['common']['book']
            file_format = args.file_format if args.file_format else config['common']['file_format']

            # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
            translator = PDFTranslator(model)
            translator.translate_pdf(pdf_file_path, file_format)
        else:
            print(OPENAI_MODEL_REQUIRED_MESSAGE)
    else:
        print(OTHER_MODEL_MESSAGE)


