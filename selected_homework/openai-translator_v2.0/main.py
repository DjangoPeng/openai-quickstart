import os
os.environ.setdefault("OPENAI_API_KEY", "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")

import json
import yaml
from flask import Flask, request, send_file

from ai_translator.translator import PDFTranslator
from ai_translator.model import GLMModel, OpenAIModel


# 创建Flask应用实例
app = Flask(__name__)


def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)


app.config.update(load_config())


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/translate", methods=["POST"])
def get_translate():
    # 获取需要翻译的文档
    if "file" not in request.files:
        return json.dumps(
            {"status": 0, "msg": "未传入文件，请检查"}
        )
    raw_file = request.files["file"]
    file_format = raw_file.content_type.split("/")[1]
    output_name = raw_file.filename + "_translated_v2." + file_format

    # 获取需要被翻译的语言
    target_language = request.form.get("language", "中文")

    if not raw_file:
        return json.dumps(
            {"status": 0, "msg": "未输入任何内容"}
        )

    #
    model = OpenAIModel(
        model=app.config["OpenAIModel"]["model"],
        api_key=app.config["OpenAIModel"]["api_key"]
    )
    #
    translator = PDFTranslator(model)
    translator.translate_pdf_v2(
        raw_file, file_format,
        output_file_path="tests/" + output_name,
        target_language=target_language
    )
    if os.path.exists("tests/" + output_name):
        return send_file("tests/" + output_name, as_attachment=True)
    else:
        return json.dumps(
            {"status": 0, "msg": "翻译异常。"}
        )


# 如果直接运行这个脚本，启动Flask应用
if __name__ == '__main__':
    app.run(debug=True, port=5000)


