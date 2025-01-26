#import langchain dependencies

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# UI
import streamlit as st

template = """
Answer the question below precisely.

Here are the conversation history: {context}

Here is the question: {question}

Answer the question.

"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# setup title
st.title("Ask LLama")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all chat history
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# build prompt input template to display prompts
prompt = st.chat_input('Type your prompt here.')

# if user hits enter
if prompt: # and prompt has stuff
    # display user msg
    st.chat_message('user').markdown(prompt)
    # store user history
    st.session_state.messages.append({"role":"user", "content":prompt})

    # llama msg
    result = chain.invoke({"context": st.session_state.messages, "question": prompt})
    # display llama msg
    st.chat_message('Llama').markdown(result)
    # store user 
    st.session_state.messages.append({"role":"Llama", "content":result})

    #print(st.session_state.messages)