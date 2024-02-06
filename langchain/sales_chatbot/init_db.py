from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import os

with open("F:\\pythonProject\\myenv\\Include\\real_estates_sale\\real_estate_sales_data.txt", encoding="utf-8") as f:
    real_estate_sales = f.read()

with open("F:\\pythonProject\\myenv\\Include\\real_estates_sale\\mobile_sales_data.txt", encoding="utf-8") as f:
    mobile_sales_data = f.read()

from langchain.text_splitter import CharacterTextSplitter

mobile_text_splitter = CharacterTextSplitter(        
    separator = '\n\n',
    chunk_size = 100,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = True,
)

mobile_docs = mobile_text_splitter.create_documents([mobile_sales_data])

text_splitter = CharacterTextSplitter(        
    separator = r'\d+\.',
    chunk_size = 100,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = True,
)
docs = text_splitter.create_documents([real_estate_sales])

for doc in docs:
    # 将问题和答案都加上 房地产销售等关键字
    doc.page_content = doc.page_content.replace("[客户问题]", "[房地产客户问题]").replace("[销售回答]", "[房地产销售回答]")
  
# 将两个doc进行合并
all_docs = mobile_docs + docs

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

db = FAISS.from_documents(all_docs, OpenAIEmbeddings())
db.save_local("real_estates_sale")

