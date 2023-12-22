import gradio as gr
import random
import time
from gradio.events import (
    Changeable,
    EventListenerMethod,
    Focusable,
    Inputable,
    Selectable,
)

from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from create_sales_vector_dbs import load_data_to_vectordb

sales_db = {
    "房产": "real_estate_sales_data",
    "电器": "sales_eletronic_stuffs"
}

def reload_sales_bot(sales_type="房产"):
    print(f"[sales_type]{sales_type}")
    global SALES_BOT
    SALES_BOT = initialize_sales_bot(sales_db[sales_type])

def initialize_sales_bot(vector_store_dir: str="real_estate_sales_data"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings())
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global SALES_BOT    
    SALES_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.8}))
    # 返回向量数据库的检索结果
    SALES_BOT.return_source_documents = True

    return SALES_BOT

def sales_chat(message, history, sales_type="房产"):
    print(f"[message]{message}")
    print(f"[history]{history}")
    print(f'''[sales_type]{sales_type}''')
    # TODO: 从命令行参数中获取
    enable_chat = True

    ans = SALES_BOT({"query": message})
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"] or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则输出套路话术
    else:
        return "这个问题我要问问领导"
    

def launch_gradio():
    global salesDemo
    salesType = gr.Dropdown(label="产品类型", choices=["房产","电器"], value="房产")

    with gr.ChatInterface(fn = sales_chat,
                          title = "销售助理",
                          additional_inputs = [
                                salesType
                            ],
                          additional_inputs_accordion_name="更多选项",
                          chatbot=gr.Chatbot(height=600)) as demo:
        
        salesType.change(reload_sales_bot, salesType)
    
    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    ##create dbs 
    load_data_to_vectordb("data/sales_eletronic_stuffs.txt", "sales_eletronic_stuffs")
    load_data_to_vectordb("data/real_estate_sales_data.txt", "real_estate_sales_data")
    # 初始化房产销售机器人
    initialize_sales_bot()
    # 启动 Gradio 服务
    launch_gradio()
