import os
from pypdf import PdfReader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

DATA_DIR = "data"
INDEX_DIR = "index"

# Load PDFs
pages = []
for pdf in os.listdir(DATA_DIR):
    if pdf.endswith(".pdf"):
        reader = PdfReader(os.path.join(DATA_DIR, pdf))
        for page in reader.pages:
            pages.append(page.extract_text())

print(f"Found {len(pages)} pages.")

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
docs = splitter.create_documents(pages)

# Embeddings
emb = OllamaEmbeddings(model="nomic-embed-text")
print("Embedding…")
faiss_store = FAISS.from_documents(docs, emb)

os.makedirs(INDEX_DIR, exist_ok=True)
faiss_store.save_local(INDEX_DIR)

print("Index saved to index/")
