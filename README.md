# What is this?
There is an open source AI model with the name Ollama. This project allows users to interact with ollama like how people interact with chatgpt, with an interface.
## How to use
### 1. Download ollama in ollama.com
### 2. Type ollama in terminal/powershell
### 3. ollama pull llama3 (<5 GB, you can try running it using *ollama run llama3* to test if it works)
### 4. pip install langchain langchain-ollama streamlit 
### 5. Create virtual environment (optional)
  - Mac/Linux: *python -m venv chatbot*,
  - Window: *python3 -m venv chatbot*
  - change chatbot to elsename if you want to
### 6. Activate virtual environment (also optional)
  - Mac/Linux: *source chatbot/bin/activate*
  - Window: *.\venv* or *.\chatbot\Scripts\activate.bat*

To run the main.py, you will need to
streamlit run [file_name] [ARGUMENTS]

For instance: 

streamlit run main.py

streamlit run stream_typing.py


![image](https://github.com/user-attachments/assets/9550a056-f810-4b64-8951-694246429363)


## Reference:

https://www.youtube.com/watch?v=d0o89z134CQ

https://www.youtube.com/watch?v=XctooiH0moI
