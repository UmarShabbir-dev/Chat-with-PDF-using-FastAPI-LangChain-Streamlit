import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from openai import OpenAI
from langchain_community.llms import OpenAI as LangOpenAI
from langchain.chains import RetrievalQA

def save_pdf_and_load(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='pdf') as tmp: 
        tmp.write(file_bytes)  # Taking the uploaded pdf file bytes content and writing it into temp file
        tmp_path = tmp.name
        
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    docs = split_documents(documents)
    
    db = embed_store_chunks(docs)

    qa_chain = process_model(db)
    return qa_chain

def split_documents(documents):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # overlap 200 characters with previous chunk
    docs = splitter.split_documents(documents)
    return docs


def embed_store_chunks(documents):
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents,embeddings)
    return db

def process_model(db):
    llm = LangOpenAI(temperature=0, openai_api_key=user_api_key)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa

apikey = None
def get_answer(qa_chain, query: str) -> str:
    return qa_chain.run(query)

user_api_key = None

def get_key(key: str) -> str:
    global user_api_key
    user_api_key = key
    return user_api_key