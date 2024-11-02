import os, json
import sys
# not sure why can't import module without it.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask,request
# open ai
from translator import PDFTranslator
from model import OpenAIModel

app = Flask(__name__)

# Upload path
UPLOAD_FOLDER = '/Users/Kelven/TempUpload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# translate the file from local dir
@app.route('/api/v1/translate/<filename>', methods=['POST'])
def file_translate(filename):

    data = request.get_data()
    # parse request data
    json_data = json.loads(data.decode('utf-8'))
    file_type = json_data.get('file_type')
    filefullname = filename + '.' + file_type
    # support request language
    target_language = json_data.get('target_language')
    target_format = json_data.get('target_format')
    
    newModel = OpenAIModel(model='gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY"))
    translator = PDFTranslator(newModel)

    # target_language not support yet 
    translator.translate_pdf(app.config['UPLOAD_FOLDER'] + filefullname, target_format)

    output_filename = app.config['UPLOAD_FOLDER'] + os.path.basename(app.config['UPLOAD_FOLDER'] + filename + "_translated.md")

    return {
        'status': 0,
        'msg': '',
        'data': output_filename
    }


if __name__ == '__main__':
    app.run(debug=True)