import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig


def translation(input_file, source_language, target_language, style, writer):
    LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}\n文体类型: {style}\n作家名字: {writer}")

    output_file_path = Translator.translate_pdf(
        input_file.name, source_language=source_language, target_language=target_language, style=style, writer=writer)

    return output_file_path

def change_writer(choice):
    if choice == "input":
        return gr.Textbox.update(visible=True, value="")
    else:
        return gr.Textbox.update(visible=False, value=choice)
     
def change_style(choice):
    if choice == "custom":
        return gr.Textbox.update(visible=True, value="")
    elif choice == "novel" or choice == "news":
        return gr.Textbox.update(visible=False, value=choice)
    else:
        return gr.Textbox.update(visible=False, value="none")
    
def launch_gradio():

    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese"),
            gr.Radio([" none", "novel", "news", ""], label="文本类型", info="Where did they go?")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

    iface.launch(share=True, server_name="0.0.0.0")

def launch_gradio_by_blocks():
    with gr.Blocks() as blocks:
        input_file = gr.File(label="上传PDF文件")
        source_language = gr.Textbox(
            label="源语言（默认：英文）", placeholder="English", value="English"
        )
        target_language = gr.Textbox(
            label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese"
        )
        style_radio = gr.Radio(["none", "novel", "news", "custom"], label="文体类型", info="选择文体类型，custom 自定义输入", value="none")
        style_text = gr.Textbox(show_label=False, lines=1, visible=False, placeholder="输入文体类型", value="none")
        style_radio.change(fn=change_style, inputs=style_radio, outputs=style_text)
        writer_radio = gr.Radio(["none", "input"], label="作家风格", info="input 自定义输入作家名字", value="none")
        writer_text = gr.Textbox(show_label=False, lines=1, visible=False, placeholder="输入作家名字", value="none")
        writer_radio.change(fn=change_writer, inputs=writer_radio, outputs=writer_text)
        output_file = gr.File(label="下载翻译文件")
        clear = gr.ClearButton(components=[input_file, source_language, target_language, style_radio, writer_radio, writer_text])
        submit = gr.Button("Submit")
        submit.click(
            translation,
            inputs=[input_file, source_language, target_language, style_text, writer_text],
            outputs=[output_file],
        )
    blocks.launch(share=True, server_name="0.0.0.0")

def initialize_translator():
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)    
    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    global Translator
    Translator = PDFTranslator(config.model_name)


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Gradio 服务
    //launch_gradio()
    launch_gradio_by_blocks()
