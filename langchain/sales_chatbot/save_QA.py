import os

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

with open("real_estate_sales_data.txt") as f:
    real_estate_sales = f.read()

text_splitter = CharacterTextSplitter(
    separator = r'\d+\.',
    chunk_size = 100,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = True,
)

docs = text_splitter.create_documents([real_estate_sales])
db = FAISS.from_documents(docs, OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")))

db.save_local("real_estates_sale")