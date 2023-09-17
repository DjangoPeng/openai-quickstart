import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A translation tool that supports translations in any language pair.')
        self.parser.add_argument('--config_file', type=str, default='config.yaml', help='Configuration file with model and API settings.')
        self.parser.add_argument('--model_name', type=str, help='Name of the Large Language Model.')
        self.parser.add_argument('--input_file', type=str, help='PDF file to translate.')
        self.parser.add_argument('--output_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
        self.parser.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
        self.parser.add_argument('--target_language', type=str, help='The target language for translating the original book.')
        self.parser.add_argument('--openai_api_key', type=str, help='The API key for OpenAIModel. Required if model_type is "OpenAIModel".')
        self.parser.add_argument('--style',type=str, help='Type a writing style you like to be translated/None ')

    def parse_arguments(self):
        args = self.parser.parse_args()
        return args
