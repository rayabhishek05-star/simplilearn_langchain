import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


open_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if not open_api_key:
    st.warning("Please enter your OpenAI API key to continue")
    st.stop()

llm = ChatOpenAI(model="gpt-5",api_key=open_api_key)
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#llm = ChatOpenAI(model="gpt-5",api_key=OPENAI_API_KEY)
title_prompt = PromptTemplate(
    input_variables = ["country"],
    template = """
    You are an experienced chef.
    You need to find the favorite cuisine for tht country: {country}
    Answer exactly with one cuisine.
    """
)

speech_prompt = PromptTemplate(
    template = """
    You need to craft a expansive meal for breakfast, lunch and dinner
    with the following cuisine: {cuisine}
    """
)

first_chain = title_prompt | llm | StrOutputParser()
second_chain = speech_prompt | llm
final_chain = first_chain | second_chain
st.title("Country Cuisine Generator App")

country = st.text_input("Enter the country:")

if country:
    response = final_chain.invoke({"country": country
    })
    st.write(response.content)
    print(response)