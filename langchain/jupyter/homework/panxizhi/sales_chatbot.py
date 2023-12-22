import argparse
import gradio as gr
import random
import time

from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

global_usingAI=None

def initialize_sales_bot(vector_store_dir: str="real_estates_sale"):
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings())
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global SALES_BOT    
    SALES_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.77,"k":3}))
    # 返回向量数据库的检索结果
    SALES_BOT.return_source_documents = True
    SALES_BOT.combine_documents_chain.verbose = True
    return SALES_BOT

def sales_chat(message, history, usingAI):
    global global_usingAI

    print(f'[global_usingAI]{global_usingAI}')
    print(f"[message]{message}")
    print(f"[history]{history}")
    print(f'[usingAI]{usingAI}')
    # TODO: 从命令行参数中获取
    enable_chat = usingAI if global_usingAI is None else global_usingAI

    ans = SALES_BOT({"query": message})
    res, source_docs= ans["result"], ans["source_documents"]
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if (source_docs and len(source_docs) > 0) or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return res
    # 否则输出套路话术
    else:
        return "这个问题我要问问领导"
    

def launch_gradio(usingAI):
    global global_usingAI
    if usingAI is not None:
        global_usingAI = True if usingAI == 1 else False

    demo = gr.ChatInterface(
        fn=sales_chat,
        title="房产销售",
        retry_btn=None,
        undo_btn=None,
        chatbot=gr.Chatbot(height=500),
        additional_inputs=[gr.Checkbox(value=True,label="AI Reply"),],
        additional_inputs_accordion_name="更多选项",
    )

    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    # 初始化房产销售机器人
    initialize_sales_bot()
    parser = argparse.ArgumentParser()
    parser.add_argument("--usingAI", type=int, help="Should use AI reply or not.")
    args = parser.parse_args()
    print(f'[args]{args}')
    # 启动 Gradio 服务
    launch_gradio(usingAI=args.usingAI)
