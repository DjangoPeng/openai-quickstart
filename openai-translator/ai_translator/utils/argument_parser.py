# 导入argparse模块，用于解析命令行参数
import argparse

# 定义一个ArgumentParser类
class ArgumentParser:
    # 初始化函数
    def __init__(self):
        # 创建一个ArgumentParser对象，设置description属性
        self.parser = argparse.ArgumentParser(description='Translate English PDF book to Chinese.')
        # 添加一个--config参数，类型为字符串，默认值为'config.yaml'，帮助信息为'包含模型和API设置的配置文件。'
        self.parser.add_argument('--config', type=str, default='config.yaml', help='Configuration file with model and API settings.')
        # 添加一个--model_type参数，类型为字符串，必填，可选值为'GLMModel'和'OpenAIModel'，帮助信息为'要使用的翻译模型类型。可选值为"GLMModel"和"OpenAIModel"。'
        self.parser.add_argument('--model_type', type=str, required=True, choices=['GLMModel', 'OpenAIModel'], help='The type of translation model to use. Choose between "GLMModel" and "OpenAIModel".')        
        # 添加一个--glm_model_url参数，类型为字符串，帮助信息为'ChatGLM模型的URL。'
        self.parser.add_argument('--glm_model_url', type=str, help='The URL of the ChatGLM model URL.')
        # 添加一个--timeout参数，类型为整数，帮助信息为'API请求的超时时间（秒）。'
        self.parser.add_argument('--timeout', type=int, help='Timeout for the API request in seconds.')
        # 添加一个--openai_model参数，类型为字符串，帮助信息为'OpenAI模型的名称。如果model_type为"OpenAIModel"，则必填。'
        self.parser.add_argument('--openai_model', type=str, help='The model name of OpenAI Model. Required if model_type is "OpenAIModel".')
        # 添加一个--openai_api_key参数，类型为字符串，帮助信息为'OpenAIModel的API密钥。如果model_type为"OpenAIModel"，则必填。'
        self.parser.add_argument('--openai_api_key', type=str, help='The API key for OpenAIModel. Required if model_type is "OpenAIModel".')
        # 添加一个--book参数，类型为字符串，帮助信息为'要翻译的PDF文件。'
        self.parser.add_argument('--book', type=str, help='PDF file to translate.')
        # 添加一个--file_format参数，类型为字符串，帮助信息为'翻译后的书籍文件格式。现在支持PDF和Markdown。'
        self.parser.add_argument('--file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')

    # 解析参数
    def parse_arguments(self):
        # 调用parse_args()方法解析参数
        args = self.parser.parse_args()
        # 如果model_type为'OpenAIModel'，但是openai_model和openai_api_key都没有设置，则抛出错误
        if args.model_type == 'OpenAIModel' and not args.openai_model and not args.openai_api_key:
            self.parser.error("--openai_model and --openai_api_key is required when using OpenAIModel")
        return args