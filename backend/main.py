from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf_utils import save_pdf_and_load, get_answer, get_key

app = FastAPI()

# Allow CORS so Streamlit can talk to this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/apikey")
async def enter_api_key(key:str):
    get_key(key)
    return {"message": "Key Added"}

qa_chain = None
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    global qa_chain
    file_bytes = await file.read()
    qa_chain = save_pdf_and_load(file_bytes)
    return {"message": "PDF processed and ready for questions!"}


@app.get("/ask/")
async def ask_question(query: str):
    if qa_chain is None:
        return {"error":"Please upload a PDF First"}
    
    answer = get_answer(qa_chain,query)
    return {"answer" : answer}

@app.get("/apikey")
async def enter_api_key(key:str):
    get_key(key)
    return {"message": "Key Added"}