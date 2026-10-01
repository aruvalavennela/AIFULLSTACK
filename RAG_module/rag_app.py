import chromadb
import streamlit as st
from ollama import chat 
from sentence_transformers import SentenceTransformer
st.set_page_config(page_title="Technova concierge",page_icon=".",layout="wide")
@st.cache_resource
def load_resources():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("fest_docs")
    return model,collection
model, collection = load_resources()
st.title("Nova, the Technova conceirge")
st.caption("I only know the fest documents. Ask me anything about Technova!")
st.session_state.setdefault("last_query","-")
st.session_state.setdefault("results",[])
with st.sidebar:
    st.header("knowledge meter")
    st.metric("Total chunks in memory",collection.count())
    st.caption("Last searched query")
    st.write(st.session_state.last_query)