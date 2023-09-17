import gradio as gr
import random
import time

from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


def initialize_children_why(vector_store_dir: str= "children_whys"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings())
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global CHILDREN_WHYS
    CHILDREN_WHYS = RetrievalQA.from_chain_type(llm,
                                                retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.8}))
    # 返回向量数据库的检索结果
    CHILDREN_WHYS.return_source_documents = True

    return CHILDREN_WHYS

def sales_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")
    enable_chat = True

    ans = CHILDREN_WHYS({"query": message})
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"] or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则输出套路话术
    else:
        return "这个问题妈妈也不知道"
    

def launch_gradio():
    demo = gr.ChatInterface(
        fn=sales_chat,
        title="儿童十万个为什么应答",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    # 初始化十万个为什么问答
    initialize_children_why()
    # 启动 Gradio 服务
    launch_gradio()
