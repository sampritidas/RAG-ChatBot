from setuptools import setup, find_packages

setup(
    name="rag_chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain>=1.0.0",
        "langchain-core>=0.2.0",
        "langchain-community>=0.2.0",
        "langchain-ollama>=1.0.0",
        "faiss-cpu",
        "pypdf",
        "python-dotenv",
        "streamlit"
    ],
    python_requires=">=3.12"
)

