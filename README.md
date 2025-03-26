# Chat-with-PDF-using-FastAPI-LangChain-Streamlit
- Upload and process any PDF
- Ask natural language questions about the document
- Uses FAISS for vector search and HuggingFace for embeddings
- Powered by OpenAI GPT models (user provides API key)
- Streamlit UI for easy interaction

  
## Tech Stack

- FastAPI
- LangChain
- OpenAI / GPT
- HuggingFace Embeddings
- FAISS
- Streamlit

---

## Requirements

- Python 3.8+
- OpenAI API Key (you'll input it yourself)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/UmarShabbir-dev/Chat-with-PDF-using-FastAPI-LangChain-Streamlit.git
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```


##  Run the App

### Terminal 1: Run FastAPI Backend
```bash
cd backend
uvicorn main:app --reload
```
Visit: http://localhost:8000/docs for Swagger API

### Terminal 2: Run Streamlit Frontend
```bash
cd frontend
streamlit run app.py
```
Visit: http://localhost:8501 to use the app

---

## Example Flow

1. Enter your OpenAI API key
2. Upload your PDF file
3. Ask a question (e.g. "What is the summary of this document?")
4. Get answers using GPT + LangChain magic 
