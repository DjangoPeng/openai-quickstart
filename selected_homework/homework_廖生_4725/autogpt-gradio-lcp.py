#安装相关依赖
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAIChat
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper #谷歌搜索api
from langchain.tools import WriteFileTool, ReadFileTool #将结果写入、读取
from langchain.vectorstores import FAISS #向量数据库
from langchain.docstore import InMemoryDocstore

import gradio
import faiss
import os

os.environ["SERPAPI_API_KEY"] = ""
os.environ["OPENAI_API_KEY"] = ""


def initAutoGPT() : 
    #1. 构造工具
    search = SerpAPIWrapper()
    tools = [Tool(name="搜索", func=search.run, description="基于当前互联网上最新消息进行搜索"), ReadFileTool(), WriteFileTool()]
    
    #2. 构造autogpt
    llm_openai = OpenAIChat()
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    
    #open ai embeding 的维度
    embedding_dim = 1536
    index = faiss.IndexFlatL2(embedding_dim)
    db_faiss = FAISS(embedding_function=embedding.embed_query, index=index, docstore=InMemoryDocstore({}),index_to_docstore_id = {})
        
    global auto_gpt
    auto_gpt = AutoGPT.from_llm_and_tools(ai_name="joel",
                                          ai_role="Assistant", 
                                          llm=llm_openai,
                                          memory=db_faiss.as_retriever(search_type="similarity_score_threshold", search_kwargs={'score_threshold': 0.8}),
                                          tools=tools)
    auto_gpt.chain.verbose = True

def query(message:str, history=[])->str:
    initAutoGPT()
    result = auto_gpt.run([message])
    
    return result
    
    
    
def launch():
    gradio_interface = gradio.ChatInterface(fn=query)
    gradio_interface.launch()

if __name__ == "__main__" :
    # initAutoGPT()
    # result = auto_gpt.run(["第一创业证券2023年度半年度利润是多少？"])
    # print(result)
    launch()