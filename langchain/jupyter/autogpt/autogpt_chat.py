import gradio as gr
import faiss
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool


def initialize_autogpt():
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

    # init vector store
    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(OpenAIEmbeddings().embed_query, index, InMemoryDocstore({}), {})

    global Agent
    Agent = AutoGPT.from_llm_and_tools(
        ai_name="Jarvis",
        ai_role="Assistant",
        tools=tools,
        llm=ChatOpenAI(temperature=0),
        memory=vectorstore.as_retriever(),
    )
    Agent.chain.verbose = True

def chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")

    ans = Agent.run(message)
    print(f"[answer is: ]{ans}")
    if ans:
        return ans
    else:
        return "No answer found"


def launch_gradio():
    demo = gr.ChatInterface(
        fn=chat,
        title="AutoGPT-Chat",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")


if __name__ == "__main__":
    initialize_autogpt()
    launch_gradio()