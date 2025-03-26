import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def save_pdf_and_load(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='pdf') as tmp: 
        tmp.write(file_bytes)  # Taking the uploaded pdf file bytes content and writing it into temp file
        tmp_path = tmp.name
        
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    docs = split_documents(documents)
    return docs

def split_documents(documents):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # overlap 200 characters with previous chunk
    docs = splitter.split_documents(documents)
    return docs

