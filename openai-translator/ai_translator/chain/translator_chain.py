import os
from ai_translator.utils import LOG

# 导入 Chat Model 即将使用的 Prompt Templates
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


class TranslatorChain:
    def __init__(self, model_name: str = "gpt-3.5-turbo", verbose: bool = True):
        system_template = (
            """你是一个翻译专家，擅长各国语言。 \n
            请将我发送给你的文字内容，翻译成{target_language}。 \n
            翻译结果以{lang_style}风格展示 \n
            """
            # 注意：\n
            # 1、保留原文间距和格式（空格，分隔符，换行符）\n
            # 2、如果原文是表格，请按照下面的表格形式返回（文字内容仍然需要翻译）：\n
            #    [Title1, Title2, Title3 ] \n
            #    [context1, context2, context3] \n

        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose,
                          openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template)

    def run(self, text: str, target_language: str, lang_style: str) -> (str, bool):
        result = ""
        try:
            result = self.chain.run(text=text, target_language=target_language, lang_style=lang_style)
        except Exception as e:
            LOG.error(f"An error occurred: {e}")
            return result, False

        return result, True

