from ollama import chat
import streamlit as st
st.set_page_config(page_title="LlamaBot App",page_icon=" ")
st.title("LlamaBot - here to talk!")

personality="you are a friendly and patient tutorr named llama. answer warmly.keep the answers with in one sentence."
personality_2="you are a good tutor . giving answers tooo quick"

if "history" not in st.session_state:
    st.session_state.history=[{"role":"system","content":personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg=None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0], icon= st.session_state.toast_msg[1])
    st.session_state.toast_msg=None

with st.sidebar:
    st.header("chat controls")
    if st.button("clear chat", type = "primary"):
        st.session_state.history=[{"role":"system","content":personality}]
        st.session_state.toast_msg=("chat cleared successfully!"," ")
        st.rerun()
    if st.button("change personality"):
        st.session_state.history[0]["content"]=personality_2
        st.session_state.toast_msg=("bot personlity changed successfully!"," ")
        st.rerun()

with st.chat_message("assistant"):
    st.write("hello! I'm llama.ask something to get started.")


for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("type something.....")
if question:
    st.session_state.history.append({"role": "user","content": question})
    with st.chat_message("user"):
        st.write(question)
    try:

        with st.spinner("thinking..."):
            response = chat(model="llama3.2", messages=st.session_state.history)
    
    
        reply = response["message"]["content"]
        st.session_state.history.append({"role": "assistant","content":reply})
        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.write("ollama is not working. try again.")