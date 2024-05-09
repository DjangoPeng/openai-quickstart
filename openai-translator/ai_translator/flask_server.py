import sys
import os
from argparse import Namespace

from model import OpenAIModel

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, send_file, jsonify
from utils import ArgumentParser, LOG, ConfigLoader
from translator import PDFTranslator

app = Flask(__name__)

TEMP_FILE_DIR = "flask_temps/"

@app.route('/translate', methods=['POST'])
def translate():
    try:
        #input_file = request.files['input_file']
        source_text = request.form.get['source_text', 'source_text']
        source_language = request.form.get('source_language', 'English')
        target_language = request.form.get('target_language', 'Chinese')

        translation_text = Translator.translate_to_text(source_text=source_text, target_language=target_language)
        response = {
            'status': 'success',
            'message': translation_text
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 400

@app.route('/translation', methods=['POST'])
def translation():
    try:
        input_file = request.files['input_file']
        source_language = request.form.get('source_language', 'English')
        target_language = request.form.get('target_language', 'Chinese')

        LOG.debug(f"[input_file]\n{input_file}")
        LOG.debug(f"[input_file.filename]\n{input_file.filename}")

        if input_file and input_file.filename:
            # # 创建临时文件
            input_file_path = TEMP_FILE_DIR + input_file.filename
            LOG.debug(f"[input_file_path]\n{input_file_path}")

            input_file.save(input_file_path)

            # 调用翻译函数
            output_file_path = Translator.translate_pdf(
                input_file=input_file_path,
                source_language=source_language,
                target_language=target_language)

            # 移除临时文件
            # os.remove(input_file_path)

            # 构造完整的文件路径
            output_file_path = os.getcwd() + "/" + output_file_path
            LOG.debug(output_file_path)

            # 返回翻译后的文件
            return send_file(output_file_path, as_attachment=True)
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 400



def initialize_translator():
    # 解析命令行
    # argument_parser = ArgumentParser()
    # args = argument_parser.parse_arguments()

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


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Flask Web Server
    app.run(host="0.0.0.0", port=5000, debug=True)