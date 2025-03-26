import tempfile
from langchain.document_loaders import PyPDFLoader

def save_pdf_and_load(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='pdf') as tmp: 
        tmp.write(file_bytes)  # Taking the uploaded pdf file bytes content and writing it into temp file
        tmp_path = tmp.name
        
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()
    
    return documents

