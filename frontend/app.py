import streamlit as st
import requests

st.set_page_config(page_title="Chat with PDF", layout="centered")

st.title("Chat with your PDF")
st.markdown("Upload a PDF and ask a question")

key = st.text_input("Enter your openai Key")

if st.button("Add") and key:
    with st.spinner("Adding..."):
        res = requests.get("http://localhost:8000/apikey", params={"key": key})
        if res.status_code == 200:
            st.success("Key Added")
        else:
            st.error(f"Error: {res.text}")

pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

if pdf_file:
    with st.spinner("Uploading and Processing PDF..."):
        files = {"file": (pdf_file.name,pdf_file,"application/pdf")}
        res = requests.post("http://localhost:8000/upload/",files=files)
        if res.status_code == 200:
            st.success("PDF uploaded successfully! You can now ask questions.")
        else:
            st.error(f"Upload failed: {res.text}")


query = st.text_input("Ask something about the PDF:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        res = requests.get("http://localhost:8000/ask", params={"query": query})
        if res.status_code == 200:
            st.markdown(f"**Answer:** {res.json()['answer']}")
        else:
            st.error(f"Error: {res.text}")