import streamlit as st
from langchain_ollama import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

st.title("🦙 Ollama Chatbot")

# Initialize Ollama model
llm = Ollama(model="llama3.1")  # change model if needed

# Session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    # Prompt template (can be customized)
    template = "Answer the question as helpfully as possible:\nQuestion: {question}\nAnswer:"
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create chain and get response
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"question": user_input})

    # Save to history
    st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
