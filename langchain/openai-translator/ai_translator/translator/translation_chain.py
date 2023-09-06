from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from utils import LOG

class TranslationChain:
    def __init__(self, model_name: str = "gpt-3.5-turbo", verbose: bool = True):
        
        # 翻译任务指令始终由 System 角色承担
        template = (
            """You are a highly experienced and capable translator, proficient in various languages. \n
            You will identify the language of the text and translate it step by step:
            Step 1. Provide a direct translation of the text from {source_language} to {target_language}.
            Step 2. Provide an explanation of any colloquialisms and differences between the direct translation and 
                     a comprehensible translation that may be confusing to a non-native speaker of the source language.
            Step 3. Understanding the translation content of Step 2 and convert it into the style of {style}."""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # 待翻译文本由 Human 角色输入
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # 使用 System 和 Human 角色的提示模板构造 ChatPromptTemplate
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        # 为了翻译结果的稳定性，将 temperature 设置为 0
        chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose)

        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

    def run(self, text: str, source_language: str, target_language: str, style: str) -> (str, bool):
        result = ""
        try:
            result = self.chain.run({
                "text": text,
                "source_language": source_language,
                "target_language": target_language,
                "style": style
            })
        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True