from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

template = """
Answer the question below precisely.

Here is the conversation history: {chat_history}

Here is the question: {question}

Answer the question.
"""

model_name = "llama3"
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model=model_name)
chain = prompt | model

st.title("Ask Llama (Streaming)")

# Initialize chat history in session state as list of messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        role = "user"  
    else:
        role = "Llama"
    st.chat_message(role).markdown(msg.content)

# User input
user_input = st.chat_input("Type your prompt here.")

if user_input:
    human_msg = HumanMessage(user_input)
    st.session_state.messages.append(human_msg)
    st.chat_message("user").markdown(user_input)

    try:
        response_gen = chain.stream({
            "chat_history": st.session_state.messages,
            "question": user_input
        })

        ai_msg_container = st.chat_message("Llama")
        full_response = ""
        # Use st.write_stream to display streaming tokens
        full_response = st.write_stream(response_gen)

        # Append AI message to history
        st.session_state.messages.append(AIMessage(full_response))
    except Exception as e:
        st.error(f"Error generating response: {e}")