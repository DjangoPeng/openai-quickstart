import gradio as gr
from translator import PDFTranslator
from model import OpenAIModel

def translate(file, language):
    # Create an instance of the OpenAIModel
    model = OpenAIModel(model='gpt-3', api_key='your_api_key')
    # Create an instance of the PDFTranslator with the model
    translator = PDFTranslator(model)
    # Translate the PDF to the target language
    translated_pdf = translator.translate_pdf(file.name, target_language=language)

    # Return the translated PDF
    return translated_pdf

iface = gr.Interface(fn=translate, inputs=["file", "text"], outputs="file")
iface.launch()