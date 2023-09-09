import sys
import os
import gradio as gr
from gradio.components import Textbox,Audio,Radio
import gradio.components as gr_comp

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator


def process_pdf(pdf_file_path, file_format, output_file_path, pages, prompt, style):
    output_folder = r"C:\Users\yanca\OneDrive - Microsoft\Desktop\大模型上课\projects\openai-quickstart\openai-translator\outputs"
    output_path = f"{output_folder}\{output_file_path}"

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path.name, file_format, output_file_path=output_path, pages=pages, prompt=prompt, style=style)
    return output_path

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()

    model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    glm_model_url = args.glm_model_url if args.glm_model_url else config['GLMModel']['model_url']
    glm_timeout = args.timeout if args.timeout else config['GLMModel']['timeout']

    model = OpenAIModel(model=model_name, api_key=api_key)

    # if args.openai_model:
    #     model = OpenAIModel(model=model_name, api_key=api_key)
    # else:
    #     model = GLMModel(model_url=glm_model_url, timeout=int(glm_timeout))

    # Define the choices you want in the dropdown
    choices = ["Translated in the style of James Joyce", 
               "Translated in the style of Ernest Miller Hemingway", 
               "Translated in the style of William Shakespeare", 
               "Translated in the style of Press Release"]

    input_interface = [
        gr_comp.File(label="Provide the PDF file path", file_count="single"),
        gr_comp.Textbox(label="File Format (e.g., PDF)"),
        gr_comp.Textbox(label="Output File Path"),
        gr_comp.Number(label="Number of Pages (optional)"),
        gr_comp.Textbox(label="Prompt"),
        gr.inputs.Dropdown(choices=choices, label="Select style option")
    ]

    # output_interface = gr.outputs.HTML(label="Translated for PDF")
    output_interface = gr_comp.File(label="Download Translated PDF")
    demo = gr.Interface(fn=process_pdf, inputs= input_interface, outputs=output_interface,
                             title="Demo For OpenAI Translator V2",
                             description="demo")

    demo.queue().launch(share=True, show_error=True)
