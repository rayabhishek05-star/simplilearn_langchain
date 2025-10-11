import os

from  langchain_community.chat_models import ChatOllama

import streamlit as st

llm = ChatOllama(model="llama3.2:latest")

st.title("Curious, Ask Anything")
question = st.text_input("Type in your question:")
if question:
    response = llm.invoke(question)
    st.write(response.content)
    print(response)
