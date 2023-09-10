import sys
import os
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig

styleMap = {
    "小说": "Novel",
    "新闻稿": "News",
    "李白风格": "LiBai-Style",
}

def translation(input_file, style_name, fiel_format, source_language, target_language):
    LOG.debug(f"[翻译任务]\n风格:{style_name}\n输出格式:{fiel_format}\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}")
    
    style_id = styleMap[style_name]
    output_file_path = Translator.translate_pdf(
        input_file.name,translate_style=style_id, output_file_format=fiel_format, source_language=source_language, target_language=target_language)

    return output_file_path

def launch_gradio():

    iface = gr.Interface(
        fn=translation,
        title="OpenAI-Translator v2.0(PDF 电子书翻译工具)",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Dropdown(label="翻译风格", choices=["小说", "新闻稿","李白风格"], value="小说"),
            gr.Dropdown(label="输出格式", choices=["PDF","Markdown"], value="PDF"),
            gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never",
        live=True
    )

    iface.launch(share=True, server_name="0.0.0.0")

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
    launch_gradio()
