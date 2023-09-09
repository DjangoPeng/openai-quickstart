from langchain.chat_models import ChatOpenAI  # 导入 ChatOpenAI 类，用于构造聊天模型
from langchain.chains import LLMChain  # 导入 LLMChain 类，用于构造 LLMChain 对象

from langchain.prompts.chat import (  # 导入聊天提示模板，用于构造 ChatPromptTemplate 对象
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from utils import LOG  # 导入 LOG 工具，用于记录日志

# 创建一个 TranslationChain 类，用于构造翻译任务的聊天模型
class TranslationChain:
    # model_name: 聊天模型的名称，默认为 gpt-3.5-turbo
    # verbose: 是否打印日志，默认为 True
    def __init__(self, model_name: str = "gpt-3.5-turbo", verbose: bool = True):

        # 使用 System 角色的提示模板，用于提示用户当前的翻译任务
        # source_language: 待翻译文本的源语言
        # target_language: 待翻译文本的目标语言
        template = (
            """You are a translation expert, proficient in various languages. \n
            Translates {source_language} to {target_language}."""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # 待翻译文本由 Human 角色输入
        # text: 待翻译的文本
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # 使用 System 和 Human 角色的提示模板构造 ChatPromptTemplate
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        # 根据 model_name 构造聊天模型，为了翻译结果的稳定性，将 temperature 设置为 0
        chat = ChatOpenAI(model_name=model_name, temperature=0, verbose=verbose)

        # 构造 LLMChain 对象
        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

    # run 方法，用于运行翻译任务，返回翻译结果和是否成功的标志
    # text: 待翻译的文本
    # source_language: 待翻译文本的源语言
    # target_language: 待翻译文本的目标语言
    def run(self, text: str, source_language: str, target_language: str) -> (str, bool):
        result = ""
        try:
            # 运行 LLMChain 对象
            result = self.chain.run({
                "text": text,
                "source_language": source_language,
                "target_language": target_language,
            })
        except Exception as e:
            LOG.error(f"An error occurred during translation: {e}")
            return result, False

        return result, True