import sys # 系统库,用于添加系统路径
import os # 操作系统库,用于处理文件路径
import gradio as gr # Gradio库,用于构建用户界面

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # 将当前文件所在目录添加到系统路径中,以便导入其他模块

# 导入 utils 模块的 ArgumentParser和LOG类，用于解析命令行参数和打印日志
from utils import ArgumentParser, LOG  

# 导入 translator 模块的 PDFTranslator和TranslationConfig类，用于翻译PDF文件
from translator import PDFTranslator, TranslationConfig

# 翻译函数，用于将PDF文件翻译为指定格式的文件
# input_file: gradio.File类型,输入文件
# source_language: str类型,源语言,默认为英语
# target_language: str类型,目标语言,默认为中文
def translation(input_file, source_language, target_language):

  # 打印调试信息
  LOG.debug(f"[翻译任务]\n源文件: {input_file.name}\n源语言: {source_language}\n目标语言: {target_language}")
  
  # 调用翻译器的translate_pdf方法进行翻译
  # input_file.name: str类型,输入文件路径
  output_file_path = Translator.translate_pdf(
    input_file.name, source_language=source_language, target_language=target_language)

  # 返回翻译后的文件路径
  return output_file_path

# 启动Gradio服务的函数  
def launch_gradio():

  # 构建界面
  # 点击提交按钮时，inputs 的值作为 fn 的参数传入
  # fn 的返回值作为 outputs 的值
  iface = gr.Interface(
    fn=translation,
    title="OpenAI-Translator v2.0(PDF电子书翻译工具)",
    inputs=[
      gr.File(label="上传PDF文件"),
      gr.Textbox(label="源语言(默认:英文)", placeholder="English", value="English"),
      gr.Textbox(label="目标语言(默认:中文)", placeholder="Chinese", value="Chinese")
    ],
    outputs=[
      gr.File(label="下载翻译文件")
    ],
    allow_flagging="never"
  )

  # 启动服务
  iface.launch(share=True, server_name="0.0.0.0")

# 初始化翻译器  
def initialize_translator():

  # 解析命令行参数
  argument_parser = ArgumentParser()
  args = argument_parser.parse_arguments()

  # 设置OpenAI API Key
  os.environ["OPENAI_API_KEY"] = args.api_key

  # 初始化配置类
  config = TranslationConfig()
  config.initialize(args)

  # 实例化翻译器对象
  global Translator
  Translator = PDFTranslator(config.model_name)

# 程序入口  
if __name__ == "__main__":
  
  # 初始化翻译器
  initialize_translator()
  
  # 启动Gradio服务
  launch_gradio()