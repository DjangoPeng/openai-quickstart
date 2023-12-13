from flask import Flask, request
from werkzeug.utils import secure_filename
from translator import PDFTranslator
from model import OpenAIModel

# Create a new Flask application
app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    """
    This function handles the POST requests to the '/translate' route.
    It expects a file and a language in the request data.
    The file is saved securely on the server and then translated to the target language.
    The translated PDF is returned as a response.

    :return: Translated PDF
    """
    # Get the file from the request
    file = request.files['file']
    # Get the target language from the request
    language = request.form.get('language')
    # Secure the filename
    filename = secure_filename(file.filename)
    # Save the file
    file.save(filename)

    # Create an instance of the OpenAIModel
    model = OpenAIModel(model='gpt-3', api_key='your_api_key')
    # Create an instance of the PDFTranslator with the model
    translator = PDFTranslator(model)
    # Translate the PDF to the target language
    translated_pdf = translator.translate_pdf(filename, target_language=language)

    # Return the translated PDF
    return translated_pdf

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)