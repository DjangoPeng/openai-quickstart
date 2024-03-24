import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model import GLMModel, OpenAIModel
from translator import PDFTranslator
from flask import Flask, render_template, request, jsonify, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = {'pdf'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 定义首页路由，用于显示翻译页面
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# 定义首页路由
@app.route('/translate', methods=['POST'])
def translate():
    # Check if POST request has file part
    if 'file' not in request.files:
        flash('No file part')
        #return render_template('index.html')
        return jsonify({"error": "No file part"})

    file = request.files['file']

    # Check if file is uploaded
    if file.filename == '':
        flash('No selected file')
        #return render_template('index.html')
        return jsonify({"error": "No selected file"})

    # Check if file type is allowed
    if file and allowed_file(file.filename):
        target_lang = request.form.get('target_lang')
        target_format = request.form.get('target_format')
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        model = OpenAIModel(model='gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY"))
        pdf_file_path = file_path
        file_format = target_format
        # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
        translator = PDFTranslator(model)
        output_file_path = translator.translate_pdf(pdf_file_path, file_format, target_lang)

        result = {
            "message": "Translation successful",
            "output_file_path": 'File saved as ' + os.path.dirname(os.path.abspath(__file__)) + '/' + output_file_path
        }
        return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
