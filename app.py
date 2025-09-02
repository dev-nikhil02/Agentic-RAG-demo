import streamlit as st
from rag_pipeline import run

st.title("Agentic RAG System Demo")

st.write(
    "This demo showcases a Retrieval-Augmented Generation (RAG) system build for Q&A on documents. "
    "Enter your financial or stock-related question on googel below, and the agent will retrieve relevant context and generate an answer."
    "Vector db of the document is stored at backend for semantic search and retrievel."
    "This model mainly focus on contextual retrieval from confidential data."
)
user_query = st.text_input("Enter your query:")

if st.button("Get Answer") and user_query:
    answer, log_entry = run(user_query)
    
    st.subheader("Answer")
    st.write(answer)
    
    st.subheader("Logs")
    with st.expander("Show logs"):
        st.text(log_entry)
