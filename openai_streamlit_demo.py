import os

from  langchain_openai import ChatOpenAI

import streamlit as st
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
llm = ChatOpenAI(model="gpt-5",api_key=OPEN_AI_KEY)

st.title("Curious, Ask Anything")
question = st.text_input("Type in your question:")
if question:
    response = llm.invoke(question)
    st.write(response.content)
    print(response)
