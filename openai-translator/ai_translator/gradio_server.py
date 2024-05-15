import sys
import os
from argparse import Namespace

import gradio as gr

from model import OpenAIModel

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG, ConfigLoader
from translator import PDFTranslator

def translation(input_file, source_language, target_language):
    LOG.debug(f"[翻译任务]\n源文件:{input_file.name}\n源语言:{source_language}\n目标语言:{target_language}")

    output_file_path = Translator.translate_pdf(input_file.name, pre_name_write, pre_name_read, file_format)

    LOG.info(f"返回路径： {output_file_path}")
    return output_file_path

def launcher_gradio():
    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v1.0(PDF电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言(默认：英文)", placeholder="English", value="English"),
            gr.Textbox(label="目标语言(默认:中文)", placeholder="Chinese", value="Chinese")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ]
    )
    iface.launch(share=True, server_name="0.0.0.0", server_port=10001)

def initialize_translator():
    #argument_parser = ArgumentParser()
    #args = argument_parser.parse_arguments()

    args = Namespace(config='config.yaml', model_type='OpenAIModel', glm_model_url=None, timeout=None,
                     openai_model='gpt-3.5-turbo', openai_api_key=None, book='tests/test.pdf', file_format='markdown',
                     pre_name_write='tests/img/', pre_name_read='img/')

    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()

    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    model = OpenAIModel(model=model_name, api_key=api_key)

    pdf_file_path = args.book if args.book else config['common']['book']
    global file_format
    file_format = args.file_format if args.file_format else config['common']['file_format']

    global pre_name_write
    pre_name_write = args.pre_name_write if args.pre_name_write else config['common']['pre_name_write']
    global pre_name_read
    pre_name_read = args.pre_name_read if args.pre_name_read else config['common']['pre_name_read']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    global Translator
    Translator = PDFTranslator(model)
   # translator.translate_pdf(pdf_file_path, pre_name_write, pre_name_read, file_format)


if __name__ == "__main__":
    initialize_translator()
    launcher_gradio()