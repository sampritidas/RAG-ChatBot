from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.docstore.document import Document

# --- Step 1: Load sample documents ---
texts = [
    "LangChain helps build LLM-based applications easily.",
    "FAISS is a library for efficient similarity search.",
    "RAG stands for Retrieval Augmented Generation."
]

# Convert to LangChain Document objects
docs = [Document(page_content=text) for text in texts]

# --- Step 2: Split text into smaller chunks (optional but recommended) ---
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
split_docs = splitter.split_documents(docs)

# --- Step 3: Create embeddings ---
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# --- Step 4: Store embeddings in FAISS ---
vectorstore = FAISS.from_documents(split_docs, embeddings)

# --- Step 5: Define a mock LLM (since we’re not using OpenAI yet) ---
def mock_llm(query, context):
    return f"[MOCK RESPONSE] Based on: {context[:100]}...\nAnswer: Simulated answer for '{query}'."

# --- Step 6: Retrieval + Mock response ---
def rag_query(query):
    results = vectorstore.similarity_search(query, k=1)
    context = results[0].page_content
    answer = mock_llm(query, context)
    print(f"🔍 Retrieved context: {context}")
    print(answer)

# --- Step 7: Test ---
rag_query("What is LangChain?")
rag_query("What is RAG?")
