import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MASAR Chatbot", page_icon="🤖")
st.title("MASRA's AI Agent 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model="gemini-2.5-flash")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask me for anything..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error {e}")