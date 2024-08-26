from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

from utils import LOG

class TranslationChain:
    def __init__(self, model_name: str = "gemma2:2b", verbose: bool = True):
        
        # 构造翻译任务提示词模板
        template = """
        You are a professional translator, skilled in a variety of areas of knowledge, renowned for rigorous content and format.

        Task:
        Translate {source_language} to {target_language} and keep the format. No more explanation.

        Source Content:
        {text}
        """
        # 构造 LangChain 提示词模板
        translation_prompt = PromptTemplate(
            input_variables=["source_language", "target_language", "text"],
            template=template,
        )

        llm = Ollama(model=model_name)
        self.chain = LLMChain(llm=llm, prompt=translation_prompt)


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