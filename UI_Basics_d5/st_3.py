import streamlit as st
import time

st. set_page_config(page_title="chatbot app Demo")

st.title("chatbot UI Demo")
with st.chat_message("user"):
    st.write("hello, I'm your assistant.TYpe something to get started")


user_message = st.chat_input("type something.............")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
        st.write(f"Hey, you wrote:{user_message},but I'm still in development.I can't reply")