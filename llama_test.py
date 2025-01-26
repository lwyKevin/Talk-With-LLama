from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below precisely.

Here are the conversation history: {context}

Here is the question: {question}

Answer the question.

"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("This ia LLama. Type anything or type exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Llama: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    handle_conversation()
