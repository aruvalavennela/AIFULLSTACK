import streamlit as st


st.set_page_config(page_title="text input Demo")
st.title("text input Demo")
name=st.text_input("enter your name:",placeholder="e.g.shanti")
st.write(f"hello,{name}!")

secret = st.text_input("enter your password:",type= "password")
st.write(f"your password has{len(secret)}characters.")

comments = st.text_area("Any additional comments?", height=150)
st.write("your wrote (len(comments))charachers.")

if st.button("submit"):
    st.write("you clicked on submit!")


show_message = st.checkbox("Do you want to proceed?")
if show_message:
    st.write("this is the message. Have a good day!")
