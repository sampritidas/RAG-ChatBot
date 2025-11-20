import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from mcp_query import query_all_mcps

INDEX_DIR = "index"

# Load FAISS index
emb = OllamaEmbeddings(model="nomic-embed-text")
db = FAISS.load_local(INDEX_DIR, emb, allow_dangerous_deserialization=True)

llm = OllamaLLM(model="llama3.1")

def rag_query(query):
    """1) Search FAISS RAG, 2) Query MCP APIs, 3) Fallback to LLM"""

    # 1️⃣ RAG
    results = db.similarity_search(query, k=4)
    context = "\n\n".join([d.page_content for d in results])

    if context.strip():
        prompt = f"""
Use this context if relevant:

{context}

Question: {query}
Answer:
"""
        answer = llm.invoke(prompt)
        if answer.strip():
            return answer

    # 2️⃣ MCP API search
    mcp_result = query_all_mcps(query)
    if mcp_result:
        return mcp_result

    # 3️⃣ LLM fallback
    return llm.invoke(query)


if __name__ == "__main__":
    while True:
        q = input("\nAsk: ")
        if q.lower() == "exit":
            break

        print("\n--- Answer ---\n")
        print(rag_query(q))
