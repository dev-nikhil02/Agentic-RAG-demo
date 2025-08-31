import streamlit as st
from rag_pipeline import run

st.title("Agentic RAG System Demo")

user_query = st.text_input("Enter your query:")

if st.button("Get Answer") and user_query:
    answer, log_entry = run(user_query)
    
    st.subheader("Answer")
    st.write(answer)
    
    st.subheader("Logs")
    with st.expander("Show logs"):
        st.text(log_entry)
