import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

# ----------------------------
# API KEYS (stored securely as environment variables)
# ----------------------------
OPENAI_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("OPEN_AI_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# ----------------------------
# Streamlit App UI
# ----------------------------
st.title("🤖 Curious — Ask Anything")
st.write("Select your favorite AI model and start chatting!")

# Dropdown to select model
model_choice = st.selectbox(
    "Choose a model:",
    ("GPT (OpenAI)", "LLaMA", "Gemini")
)

# Text input for user question
question = st.text_input("Type in your question:")

# ----------------------------
# Model Selection Logic
# ----------------------------
llm = None

if model_choice == "GPT (OpenAI)":
    if not OPENAI_KEY:
        st.error("❌ OPENAI_API_KEY not found in environment variables.")
    else:
        llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_KEY)

elif model_choice == "LLaMA":
    # Placeholder for LLaMA (Meta) integration
    llm = ChatOllama(model="llama3.2:latest")

elif model_choice == "Gemini":
    if not GEMINI_KEY:
        st.error("❌ GEMINI_API_KEY not found in environment variables.")
    else:
        # Placeholder for Google Gemini integration
        st.info("🌟 Gemini model integration placeholder.")
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=GEMINI_KEY)

# ----------------------------
# Run the selected model
# ----------------------------
if question and llm:
    with st.spinner("Thinking..."):
        response = llm.invoke(question)
        st.success("✅ Answer:")
        st.write(response.content)
