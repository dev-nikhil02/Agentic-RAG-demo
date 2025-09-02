import streamlit as st
from rag_pipeline import run

st.title("Agentic RAG System Demo")

st.markdown("""
<span style='font-size:18px'>
<ul>
<li>Ask finance or stock questions about your documents.</li>
<li>The agent finds context and answers using a vector database.</li>
<li>Designed for secure, context-aware Q&amp;A.</li>
</ul>
</span>
""", unsafe_allow_html=True)
user_query = st.text_input("Enter your query:")

if st.button("Get Answer") and user_query:
    answer, log_entry = run(user_query)
    
    st.subheader("Answer")
    st.write(answer)
    
    st.subheader("Logs")
    with st.expander("Show logs"):
        st.text(log_entry)
