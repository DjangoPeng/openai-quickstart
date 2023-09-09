import sys  # 导入sys模块，用于添加系统路径
import os  # 导入os模块，用于获取文件路径

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前文件所在目录添加到系统路径中，以便导入其他模块

from flask import Flask, request, send_file, jsonify  # 导入Flask框架中的Flask、request、send_file和jsonify模块，用于创建Flask应用实例、接收请求、发送文件和返回JSON数据
from translator import PDFTranslator, TranslationConfig  # 导入自定义的PDFTranslator和TranslationConfig类，用于翻译PDF文件
from utils import ArgumentParser, LOG  # 导入自定义的ArgumentParser和LOG函数，用于解析命令行参数和打印日志

app = Flask(__name__)  # 创建Flask应用实例

TEMP_FILE_DIR = "flask_temps/"  # 定义临时文件目录

# 使用 Flask 装饰器语法，将该函数绑定到 /translation 路径上，并指定请求方法为 POST。
@app.route('/translation', methods=['POST'])
def translation():
    try:
        # 获取上传的文件
        input_file = request.files['input_file']
        # 获取源语言和目标语言
        source_language = request.form.get('source_language', 'English')
        target_language = request.form.get('target_language', 'Chinese')

        # 打印上传文件的信息
        LOG.debug(f"[input_file]\n{input_file}")
        LOG.debug(f"[input_file.filename]\n{input_file.filename}")

        # 判断上传的文件是否存在
        if input_file and input_file.filename:
            # 创建临时文件
            input_file_path = TEMP_FILE_DIR+input_file.filename
            LOG.debug(f"[input_file_path]\n{input_file_path}")

            # 保存上传的文件到临时文件夹
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
        # 返回错误信息
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 400

def initialize_translator():
    # 解析命令行参数
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 设置 OpenAI API Key
    os.environ["OPENAI_API_KEY"] = args.api_key    

    # 初始化配置
    config = TranslationConfig()
    config.initialize(args)    
    # 初始化全局变量 Translator
    global Translator
    Translator = PDFTranslator(config.model_name)


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Flask Web Server
    app.run(host="0.0.0.0", port=5000, debug=True)