import streamlit as st
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

st.set_page_config(page_title="PDF RAG Chatbot", layout="wide")

st.title("📘 PDF RAG Chatbot (Ollama + FAISS + LangChain v1)")

# Load embeddings
embeddings = OllamaEmbeddings(model="llama3.1")

# Load FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Load LLM
llm = ChatOllama(model="llama3.1")

# Build RAG chain manually
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Use the following retrieved context to answer.

Context:
{context}

Question: {question}
""")

rag_chain = (
    RunnableParallel(
        context=retriever,
        question=RunnablePassthrough()
    )
    | prompt
    | llm
)

# UI input
question = st.text_input("Ask something from your PDFs:")

if question:
    with st.spinner("Thinking..."):
        response = rag_chain.invoke(question)

    st.markdown("### 📥 Answer")
    st.write(response.content)
