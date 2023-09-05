import gradio as gr

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.router import MultiRetrievalQAChain


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
    # SALES_BOT.return_source_documents = True

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
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")


if __name__ == "__main__":
    initialize_sales_bot()
    launch_gradio()
