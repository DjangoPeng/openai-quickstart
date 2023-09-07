import gradio as gr

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.router import MultiRetrievalQAChain
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

from typing import Any, Dict, List, Mapping, Optional

from langchain.chains import ConversationChain
from langchain.chains.base import Chain
from langchain.chains.conversation.prompt import DEFAULT_TEMPLATE
from langchain.chains.retrieval_qa.base import BaseRetrievalQA, RetrievalQA
from langchain.chains.router.base import MultiRouteChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_retrieval_prompt import (
    MULTI_RETRIEVAL_ROUTER_TEMPLATE,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import BaseRetriever
from langchain.schema.language_model import BaseLanguageModel


def initialize_sales_bot():
    db_estates = FAISS.load_local("real_estates_sale", OpenAIEmbeddings())
    db_household_apps = FAISS.load_local("household_appliances_sale", OpenAIEmbeddings())
    retriever_infos = [
        {
            "name": "real estate sale",
            "description": "Good for answering questions about the real estate sale",
            "retriever": db_estates.as_retriever(search_type="similarity_score_threshold",
                                                 search_kwargs={"score_threshold": 0.8})
        },
        {
            "name": "household appliances sale",
            "description": "Good for answering questions about household appliances sale",
            "retriever": db_household_apps.as_retriever(search_type="similarity_score_threshold",
                                                        search_kwargs={"score_threshold": 0.8})
        }
    ]

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    global SALES_BOT
    # Dynamically select from multiple retrievers
    # https://python.langchain.com/docs/use_cases/question_answering/how_to/multi_retrieval_qa_router
    SALES_BOT = MultiRetrievalQAChain.from_retrievers(llm, retriever_infos, verbose=True)

    return SALES_BOT

class MultiRetrievalQAChainV3(MultiRouteChain):
    router_chain: LLMRouterChain
    """Chain for deciding a destination chain and the input to it."""
    destination_chains: Mapping[str, BaseRetrievalQA]
    """Map of name to candidate chains that inputs can be routed to."""
    default_chain: Chain
    """Default chain to use when router doesn't map input to one of the destinations."""

    @property
    def output_keys(self) -> List[str]:
        return ["result"]

    @classmethod
    def from_retrievers(
        cls,
        llm: BaseLanguageModel,
        retriever_infos: List[Dict[str, Any]],
        default_retriever: Optional[BaseRetriever] = None,
        default_prompt: Optional[PromptTemplate] = None,
        default_chain: Optional[Chain] = None,
        **kwargs: Any,
    ) -> MultiRetrievalQAChain:
        if default_prompt and not default_retriever:
            raise ValueError(
                "`default_retriever` must be specified if `default_prompt` is "
                "provided. Received only `default_prompt`."
            )
        destinations = [f"{r['name']}: {r['description']}" for r in retriever_infos]
        destinations_str = "\n".join(destinations)
        router_template = MULTI_RETRIEVAL_ROUTER_TEMPLATE.format(
            destinations=destinations_str
        )
        router_prompt = PromptTemplate(
            template=router_template,
            input_variables=["input"],
            output_parser=RouterOutputParser(next_inputs_inner_key="query"),
        )
        router_chain = LLMRouterChain.from_llm(llm, router_prompt)
        destination_chains = {}
        for r_info in retriever_infos:
            prompt = r_info.get("prompt")
            retriever = r_info["retriever"]
            chain = RetrievalQA.from_chain_type(llm, retriever=retriever, return_source_documents=True)#.from_llm(llm, prompt=prompt, retriever=retriever, return_source_documents=True)
            name = r_info["name"]
            destination_chains[name] = chain
        if default_chain:
            _default_chain = default_chain
        elif default_retriever:
            _default_chain = RetrievalQA.from_llm(
                llm, prompt=default_prompt, retriever=default_retriever
            )
        else:
            prompt_template = DEFAULT_TEMPLATE.replace("input", "query")
            prompt = PromptTemplate(
                template=prompt_template, input_variables=["history", "query"]
            )
            _default_chain = ConversationChain(
                llm=ChatOpenAI(), prompt=prompt, input_key="query", output_key="result"
            )
        return cls(
            router_chain=router_chain,
            destination_chains=destination_chains,
            default_chain=_default_chain,
            **kwargs,
        )

def initialize_sales_botV3():
    db_estates = (FAISS.load_local("real_estates_sale", OpenAIEmbeddings())
                  .as_retriever(search_type="similarity_score_threshold",
                                search_kwargs={"score_threshold": 0.8}))
    db_household_apps = (FAISS.load_local("household_appliances_sale", OpenAIEmbeddings())
                         .as_retriever(search_type="similarity_score_threshold",
                                search_kwargs={"score_threshold": 0.8}))
    retriever_infos = [
        {
            "name": "real estate sale",
            "description": "You are a great estates sale. You are good at answering estates sale questions" +
                        "The reason why you are so excellent is that you can break down difficult problems into their constituent parts, "+
                        "answer these parts first, and then integrate them to answer more general",
            "retriever": db_estates,
        },
        {
            "name": "household appliances sale",
            "description": "You are a great household appliances sale. You are good at answering household appliances sale questions." +
                            "The reason why you are so excellent is that you can break down difficult problems into their constituent parts, " +
                            "answer these parts first, and then integrate them to answer more general",
            "retriever": db_household_apps,
        }
    ]

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    global SALES_BOT
    SALES_BOT = MultiRetrievalQAChainV3.from_retrievers(llm, retriever_infos, verbose=True)

    return SALES_BOT


def initialize_sales_botV2():
    db_estates = FAISS.load_local("real_estates_sale", OpenAIEmbeddings())
    db_household_apps = FAISS.load_local("household_appliances_sale", OpenAIEmbeddings())
    estate_template = """You are a great estates sale. You are good at answering estates sale questions. 
    The reason why you are so excellent is that you can break down difficult problems into their constituent parts, 
    answer these parts first, and then integrate them to answer more general 
    
    Question: 
    {input}"""
    household_template = """You are a great household appliances sale. You are good at answering household appliances sale questions.
    The reason why you are so excellent is that you can break down difficult problems into their constituent parts, 
    answer these parts first, and then integrate them to answer more general 
    
    Question: 
    {input}"""
    retriever_infos = [
        {
            "name": "real estate sale",
            "description": "Good for answering questions about the real estate sale",
            "retriever": db_estates.as_retriever(search_type="similarity_score_threshold",
                                                 search_kwargs={"score_threshold": 0.8}),
            "prompt_template": estate_template
        },
        {
            "name": "household appliances sale",
            "description": "Good for answering questions about household appliances sale",
            "retriever": db_household_apps.as_retriever(search_type="similarity_score_threshold",
                                                        search_kwargs={"score_threshold": 0.8}),
            "prompt_template": household_template
        }
    ]

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    destination_chains = {}
    for p_info in retriever_infos:
        name = p_info["name"]
        prompt_template = p_info.get("prompt_template")
        prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
        chain = RetrievalQA.from_llm(llm, prompt=prompt, retriever=p_info["retriever"])
        chain.return_source_documents = True
        destination_chains[name] = chain

    default_chain = ConversationChain(llm=llm, output_key="text")

    destinations = [f"{p['name']}: {p['description']}" for p in retriever_infos]
    destinations_str = "\n".join(destinations)
    router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
    router_prompt = PromptTemplate(
        template=router_template,
        input_variables=["input"],
        output_parser=RouterOutputParser(next_inputs_inner_key="query"),
    )
    router_chain = LLMRouterChain.from_llm(llm, router_prompt)

    global SALES_BOT
    SALES_BOT = MultiRouteChain(
        router_chain=router_chain,
        destination_chains=destination_chains,
        default_chain=default_chain,
        verbose=True,
    )

    return SALES_BOT

def sales_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")

    ans = SALES_BOT.run(message)
    print(f"[answer is: ]{ans}")
    if ans:
        return ans
    else:
        return "这个问题我要问问领导"


def launch_gradio():
    demo = gr.ChatInterface(
        fn=sales_chat,
        title="房产/电器销售",
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")


if __name__ == "__main__":
    initialize_sales_botV3()
    launch_gradio()
