import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from openai import OpenAI
from langchain.llms import OpenAI as LangOpenAI
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
import os

load_dotenv()

def save_pdf_and_load(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='pdf') as tmp: 
        tmp.write(file_bytes)  # Taking the uploaded pdf file bytes content and writing it into temp file
        tmp_path = tmp.name
        
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    docs = split_documents(documents)
    
    db = embed_store_chunks(docs)
    return db

def split_documents(documents):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # overlap 200 characters with previous chunk
    docs = splitter.split_documents(documents)
    return docs


def embed_store_chunks(documents):
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents,embeddings)
    return db

def process_model(db):
    llm = LangOpenAI(temperature=0,openai_api_key=os.getenv("OPENAI_API_KEY"))
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa