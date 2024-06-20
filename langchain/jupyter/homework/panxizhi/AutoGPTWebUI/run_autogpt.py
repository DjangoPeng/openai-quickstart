import os
import uuid
import faiss

from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.chat_models import ChatOpenAI

os.environ["SERPAPI_API_KEY"] = "25409e23ca5020b5264e40a5e3594f50a7ef8ee912a35f86e7ef0fde598dbd7c"

class LCAutoGPTRunner:
    agent = None

    def __init__(self):
        # 构造 AutoGPT 的工具集
        search = SerpAPIWrapper()
        tools = [
            Tool(
                name="search",
                func=search.run,
                description="useful for when you need to answer questions about current events. You should ask targeted questions",
            ),
            WriteFileTool(),
            ReadFileTool(),
        ]

        embeddings_model = OpenAIEmbeddings()

        # OpenAI Embedding 向量维数
        embedding_size = 1536
        # 使用 Faiss 的 IndexFlatL2 索引
        index = faiss.IndexFlatL2(embedding_size)
        # 实例化 Faiss 向量数据库
        vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

        agent = AutoGPT.from_llm_and_tools(
            ai_name="Jarvis",
            ai_role="Assistant",
            tools=tools,
            llm=ChatOpenAI(temperature=0),
            memory=vectorstore.as_retriever(), # 实例化 Faiss 的 VectorStoreRetriever
        )
        agent.chain.verbose = True
        self.agent = agent

    def run(self, task):
        #run the model and return the result
        rand = uuid.uuid4()
        tasks = [f'{task} Then write file to "result-{rand}.txt"']
        result = self.agent.run(tasks)
        print(f'AutoGPT result: {result}')
        return f"result-{rand}.txt"