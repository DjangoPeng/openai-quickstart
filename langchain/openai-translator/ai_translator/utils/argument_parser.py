# 导入argparse模块，用于解析命令行参数
import argparse

# 定义一个ArgumentParser类
class ArgumentParser:
    # 初始化函数，创建一个ArgumentParser对象
    def __init__(self):
        # 创建一个ArgumentParser对象，设置description属性
        self.parser = argparse.ArgumentParser(description='A translation tool that supports translations in any language pair.')
        # 添加一个config_file参数，类型为字符串，默认值为'config.yaml'，帮助信息为'Configuration file with model and API settings.'
        self.parser.add_argument('--config_file', type=str, default='config.yaml', help='Configuration file with model and API settings.')
        # 添加一个model_name参数，类型为字符串，帮助信息为'Name of the Large Language Model.'
        self.parser.add_argument('--model_name', type=str, help='Name of the Large Language Model.')
        # 添加一个api_key参数，类型为字符串，帮助信息为'The API key for OpenAIModel.'
        self.parser.add_argument('--api_key', type=str, help='The API key for OpenAIModel.')
        # 添加一个input_file参数，类型为字符串，帮助信息为'PDF file to translate.'
        self.parser.add_argument('--input_file', type=str, help='PDF file to translate.')
        # 添加一个output_file_format参数，类型为字符串，帮助信息为'The file format of translated book. Now supporting PDF and Markdown'
        self.parser.add_argument('--output_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
        # 添加一个source_language参数，类型为字符串，帮助信息为'The language of the original book to be translated.'
        self.parser.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
        # 添加一个target_language参数，类型为字符串，帮助信息为'The target language for translating the original book.'
        self.parser.add_argument('--target_language', type=str, help='The target language for translating the original book.')

    # 解析参数的函数
    def parse_arguments(self):
        # 调用ArgumentParser对象的parse_args()方法解析参数，并返回解析结果
        args = self.parser.parse_args()
        return args