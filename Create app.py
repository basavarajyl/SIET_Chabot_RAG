import streamlit as st
from rag_engine import load_base, ask_rag
st.set_page_config(page_title = "SIET_chstbot",layout = "centered")
st.title("Shridevi Institute of Engineering and Technology - ChatBpot")
st.caption("Ask anything about collage infromation...")
st.caption("Created by Basavaraju")

mykey = st.secrets("GROQ_API_KEY)
                   
@st.cache_resource
def intiate_rag():
  return load_base("01_College_Information")
 
  index, embed_model,chunk = initiate_rag()

if "chat_hist" not in st.session_state:
  st.session_state.chat_hist = []

for qa in  st.session_state.chat_hist :
  with st.chat_message(qa["role"]):
    st.write(qa["content"])


question = st.chat_input("Sak anything about SIET collage...")
if question:
  st.session_state.chat_hist.append(
    {"role" :"user" ,content = question})
  with st.chat_message("user"):
    st.write(question)

with st.chat_message("assistant"):
  with st.spinner("Asking RAG for answer...."):
    answer = ask_rag (question, embed_model, chunks, index, api_key = mykey , num_chunks)
    st.write(answer)

if st.button("Cler chat"):
  st.session_state.chat_hist = []
  st.return()
  
  
