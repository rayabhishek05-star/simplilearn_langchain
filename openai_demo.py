import os

from  langchain_openai import ChatOpenAI
from langchain_openai import OpenAI

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
llm = ChatOpenAI(model="gpt-5",api_key=OPEN_AI_KEY)

question = input("Enter your question:")
response = llm.invoke(question)
print(response)
