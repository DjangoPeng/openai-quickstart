from langchain_openai import ChatOpenAI
# 旧代码
# from langchain.chains import LLMChain

# 新代码
from langchain.globals import set_verbose
from langchain.globals import set_debug

set_verbose(False)

from utils import LOG
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

class TranslationChain:
    def __init__(self, model_name: str = "gpt-3.5-turbo", verbose: bool = True):
        
        # 翻译任务指令始终由 System 角色承担
        template = (
            """You are a translation expert, proficient in various languages. \n
            Translates {source_language} to {target_language}."""
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

        # 旧代码
        # self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

        # 新代码
        set_debug(verbose)
        self.chain = chat_prompt_template | chat

    def run(self, text: str, source_language: str, target_language: str) -> (str, bool):
        result = ""
        try:
            # 新代码
            result = self.chain.invoke({
                "text": text,
                "source_language": source_language,
                "target_language": target_language,
            }).content
            # 旧代码
            # result = self.chain.run({
            #     "text": text,
            #     "source_language": source_language,
            #     "target_language": target_language,
            # })

        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True