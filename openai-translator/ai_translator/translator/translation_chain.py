from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_community.chat_models.zhipuai import ChatZhipuAI

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from utils import LOG

class TranslationChain:
    def __init__(self, model_name: str = "glm-4", verbose: bool = True):
        
        # 翻译任务指令始终由 System 角色承担
        template = (
            """You are a translation expert, proficient in various languages.When you translate something,you can only return the contents you translate,
             without any unnecessary words. \n
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
        # 默认chatGLM，若传入openai则用ChatOpenAI，记录选择的模型
        chat = ChatZhipuAI(model_name=model_name, temperature=0,do_sample = False, verbose=verbose)
        if model_name[:3] == 'gpt':
            chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose)
        LOG.info(f"选择翻译的模型：{model_name}")

        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

    def run(self, text: str, source_language: str, target_language: str) -> (str, bool):
        result = ""
        try:
            result = self.chain.run({
                "text": text,
                "source_language": source_language,
                "target_language": target_language,
            })
        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True