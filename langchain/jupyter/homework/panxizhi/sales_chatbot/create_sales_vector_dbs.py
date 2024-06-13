from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

from langchain.text_splitter import CharacterTextSplitter

def load_data_to_vectordb(file, db_name):
    with open(file, encoding='utf8') as f:
        text = f.read()

    text_splitter = CharacterTextSplitter(        
        separator = r'$\d+\.\n',
        chunk_size = 0,
        chunk_overlap  = 0,
        length_function = len,
        is_separator_regex = True,
    )
    docs = text_splitter.create_documents([text])

    db = FAISS.from_documents(docs, OpenAIEmbeddings())

    db.save_local(db_name)

if __name__ == "__main__":
    load_data_to_vectordb("data/sales_eletronic_stuffs.txt", "sales_eletronic_stuffs")
    load_data_to_vectordb("data/real_estate_sales_data.txt", "real_estate_sales_data")