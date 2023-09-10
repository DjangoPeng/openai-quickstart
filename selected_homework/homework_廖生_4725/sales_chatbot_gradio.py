from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate

import os
import gradio as gr
    
db_name_str = ""
db_path_str = ""
def __init__(db_path:str = "", content_text_path:str = "", open_ai_key_str="")->None:
    db_path_local = db_path
    if len(db_path_local) < 0 :
        print("未输入数据库路径，无法初始化")
        return 
    
    global global_db
    global_db = None 
    db_name_local = "" 
    db_director_local = ""
    exist_path = os.path.exists(db_path_local)
    if exist_path is not True:
        content_text_path_local = content_text_path
        if len(content_text_path_local) < 0 :
            print("未输入embedding数据源头路径，无法初始化")
            return 
        
        db_str_splitters = db_path_local.split("/")
        if len(db_str_splitters) < 0 :
            print("数据库路径无效，请重新输入")
            return 
        db_name_local = db_str_splitters.pop()
        if db_name_local.endswith(".faiss") :
            db_name_local = db_name_local.split(".faiss")[0]
        db_director_local = db_path_local.split(db_name_local)[0]
        if init_vectorstore(content_path=content_text_path, db_name=db_name_local, db_directory_path=db_director_local, open_ai_key=open_ai_key_str) is not True :
            print("构建向量数据库失败，请重试")
            return 
    
    
    if db_name_local == "" :
        db_str_splitters = db_path_local.split("/")
        if len(db_str_splitters) < 0 :
            print("数据库路径无效，请重新输入")
            return 
        db_name_local = db_str_splitters.pop()
        if db_name_local.endswith(".faiss") :
            db_name_local = db_name_local.split(".faiss")[0]
        db_director_local = db_path_local.split(db_name_local)[0]
    
    embedding = OpenAIEmbeddings(openai_api_key=open_ai_key_str)
    if global_db is None:
      global_db = FAISS.load_local(folder_path=db_director_local, index_name=db_name_local, embeddings=embedding)
    
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=open_ai_key_str)
    retriver = global_db.as_retriever(search_type="similarity_score_threshold", search_kwargs={'score_threshold':0.8})
    
    global retriverChain
    retriverChain = RetrievalQA.from_chain_type(llm=llm, retriever=retriver)
    retriverChain.return_source_documents = True 
    

    prompt_template = PromptTemplate.from_template("""你作为一名专业的房产销售顾问，拥有丰富的销售经验，并掌握各种销售话术。请深入理解提供的内容(提供的内容以<开始，以>结束)
                                                   <您好，我是前海特区的壹湾臻邸的销售顾问王顾问，您可以称呼我为小王。我向您介绍以下房产信息:前海是承载了经济特区，粤港澳大湾区，深圳先行示范区，自贸试验区和深港合作区的国家核心战略平台，
是湾区最浓缩最精华的核心引擎，也是中国对话世界的力量。其中前湾占位前海三湾C位，纵向与桂湾、妈湾联动，横向与宝中、深圳湾后海互通，大前海发展全方位的价值资源聚拢于此壹湾臻邸位于前海前湾片区，聚拢链接了前海的规划、产业、配套等资源，接下来我们就一起来看一下项目的配套有哪些吧。
【 交 通 】壹湾臻邸项目位置还是挺不错的，临近 地铁5号线 “前海站”、“前海公园站”，步行时间岳不需要很久，项目北侧临近 听海大道，周边还有 沿江高速、梦海大道、前海大道 等城市道路，地铁、自驾出行相对便捷。
【 商 业 】项目 自带4000㎡商业体积，距离 前湾九单元05街坊2.35万㎡商业 500米。中集前海国际8万㎡多元体商业，将以 “Mall+Street+Park” 三重叠加场景为核心，打造24h不打烊的沉浸式商业体验空间。附近还有 前海嘉里中心商业，相信未来商业配套不会差。
【 教 育 】项目隔壁就是一块规划的 9年一贯制公立学校，目前还没有确定是哪家教育集团办学。距离项目不远是在建的 南二外前海教育集团(前湾学校)，前期上学会在这所学校，附近还有国际学校 哈罗公学>
根据用户的输入{query}, 结合提供的内容的理解，如果以上内容能提供问题的答案，则尽可能简单明了的提供答案，否则你根据问题的意思，用最简洁的内容回答。
要求：1. 如果问题与以上内容相关，则应该贴合以上内容的理解，用人性化的话语回答，否则根据根据问题的理解，尽可能用简短的语言回答，不要回答与问题不相关的内容。
2. 回答的内容要经过润色，让对方认为你就是一个人，而非机器。
3. 回答的内容简洁明了，杜绝胡编乱造""")
    global llmChain
    llmChain = LLMChain(llm=llm, prompt=prompt_template)
    
    check_template = PromptTemplate.from_template("""请深入理解提供的内容(提供的内容以<开始，以>结束)
                                                   <您好，我是前海特区的壹湾臻邸的销售顾问王顾问，您可以称呼我为小王。我向您介绍以下房产信息:前海是承载了经济特区，粤港澳大湾区，深圳先行示范区，自贸试验区和深港合作区的国家核心战略平台，
是湾区最浓缩最精华的核心引擎，也是中国对话世界的力量。其中前湾占位前海三湾C位，纵向与桂湾、妈湾联动，横向与宝中、深圳湾后海互通，大前海发展全方位的价值资源聚拢于此壹湾臻邸位于前海前湾片区，聚拢链接了前海的规划、产业、配套等资源，接下来我们就一起来看一下项目的配套有哪些吧。
【 交 通 】壹湾臻邸项目位置还是挺不错的，临近 地铁5号线 “前海站”、“前海公园站”，步行时间岳不需要很久，项目北侧临近 听海大道，周边还有 沿江高速、梦海大道、前海大道 等城市道路，地铁、自驾出行相对便捷。
【 商 业 】项目 自带4000㎡商业体积，距离 前湾九单元05街坊2.35万㎡商业 500米。中集前海国际8万㎡多元体商业，将以 “Mall+Street+Park” 三重叠加场景为核心，打造24h不打烊的沉浸式商业体验空间。附近还有 前海嘉里中心商业，相信未来商业配套不会差。
【 教 育 】项目隔壁就是一块规划的 9年一贯制公立学校，目前还没有确定是哪家教育集团办学。距离项目不远是在建的 南二外前海教育集团(前湾学校)，前期上学会在这所学校，附近还有国际学校 哈罗公学>
根据用户的输入{query}, 结合提供的内容的理解，判断问的内容是否与提供的内容强相关，如果强相关，则回答是的，否则回答不是""")
    global checkLLMChain
    checkLLMChain = LLMChain(llm = llm, prompt=check_template)
    
def init_vectorstore(content_path:str, db_name="index", db_directory_path="./langchain/sales_chatbot/", open_ai_key="")->bool:
    #传入参数有问题或者文件不存在，则直接返回
    if len(content_path) < 0 or os.path.exists(content_path) is None:
        return False
    
    #开始加载文本内容
    text_loader = TextLoader(content_path)
    texts = text_loader.load()
    
    if len(texts) < 0 :
        return False
    
    #开始分隔
    text_splitter = CharacterTextSplitter(chunk_size= 100, chunk_overlap= 0, length_function= len)
    text_splitter_list = text_splitter.split_text(texts[0].page_content)
    
    #开始embeding
    global db_name_str
    db_name_str = db_name
    global db_path_str
    db_path_str = db_directory_path
    if len(db_name) > 0 :
        db_name_str = db_name
        
    try:
        embedding = OpenAIEmbeddings(openai_api_key=open_ai_key)
        global_db = FAISS.from_texts(text_splitter_list, embedding)
        global_db.save_local(folder_path=db_path_str, index_name=db_name_str)
    except Exception as e:
        return False
    finally:
        return True
    
def add_qa(qa:str) :
    global_db.add_texts([qa])
    global_db.save_local(folder_path=db_path_str, index_name=db_name_str)
    
def llm_query(message:str, history=[])->str :
    result = llmChain({"query":message})
    print(f"[llm回答]:{result}")
    
    answer = result["text"]
    return answer

def llm_check(answer:str, history=[])->str :
    result = checkLLMChain({"query":answer})
    print(f"[llmcheck回答]:{result}")
    
    answer = result["text"]
    return answer
    

def query(message:str, history=None)->str:
    result = retriverChain({"query":message})
    print(f"[问题]:{result['query']}")
    print(f"[答案]:{result['result']}")
    
    answer = result["result"]
    if len(result["source_documents"]) <= 0 :
        answer = llm_query(message=message)
        if llm_check(answer=answer) != "是的":
            qa = "问："+message + "\n答：" + answer
            print(f"开始加入知识库:{qa}")
            add_qa(qa)
            
    return answer

def launch_gradio():
    chat_ui = gr.ChatInterface(fn=query)
    chat_ui.launch()

if __name__ == "__main__" : 
    __init__(db_path="./langchain/sales_chatbot/qa.faiss",
             content_text_path="./langchain/sales_chatbot/sz_ywzd_note.txt",
             open_ai_key_str="")
    
    launch_gradio()