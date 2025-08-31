from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer

db_path = "chroma_db"
st_model = SentenceTransformer("all-MiniLM-L6-v2")
class ExistingSTWrapper:
    def embed_documents(self, docs):
        # encode a list of documents → list of lists
        return st_model.encode(docs, convert_to_numpy=True).tolist()
    
    def embed_query(self, query):
        # encode a single query → single vector
        return st_model.encode([query], convert_to_numpy=True).tolist()[0]

embed_model = ExistingSTWrapper()



retriever_reports = Chroma(
    collection_name="annual_reports",
    embedding_function=embed_model,
    persist_directory=db_path,
).as_retriever(search_kwargs={"k": 3})

retriever_stock = Chroma(
    collection_name="stock_prices",
    embedding_function=embed_model,
    persist_directory=db_path,
).as_retriever(search_kwargs={"k": 3})


def simple_planner(query):
    query_lower = query.lower()
    if "revenue" in query_lower or "profit" in query_lower:
        return "annual_reports"
    elif "stock" in query_lower or "price" in query_lower:
        return "stock_prices"
    else:
        return "both"
    

def get_retriever_docs(user_query, retriever_reports, retriever_stock):
# --- Planner ---
    collection_choice = simple_planner(user_query)
    
    # --- Retriever ---
    if collection_choice == "annual_reports":
        docs = retriever_reports.get_relevant_documents(user_query)
    elif collection_choice == "stock_prices":
        docs = retriever_stock.get_relevant_documents(user_query)
    else:  # fallback to combine both
        docs_reports = retriever_reports.get_relevant_documents(user_query)
        docs_stock = retriever_stock.get_relevant_documents(user_query)
        docs = docs_reports + docs_stock
    
    return docs


def build_llm_prompt(docs, user_query):
    context_with_sources = ""
    for doc in docs:
        source_name = doc.metadata.get("source_file", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        snippet = doc.page_content[:300]  # first 300 characters
        context_with_sources += f"[Source: {source_name}, Chunk: {chunk_id}] {snippet}\n\n"

    prompt = f"""
You are an expert financial assistant. 
Use mostly following context to answer the question.
Don't ask questions.

Context:
{context_with_sources}

Question:
{user_query}

Answer:
"""
    return prompt


def is_high_confidence(docs, threshold=0.6):
    if not docs:
        return False
    top_score = max(doc.metadata.get("similarity", 0) for doc in docs)
    return top_score >= threshold


# def human_review(answer):
#     print("\n--- HUMAN REVIEW REQUIRED ---")
#     print("Suggested answer:\n", answer)
#     confirm = input("\nDo you approve this answer? (y/n): ").strip().lower()
#     if confirm == "y":
#         print("Answer approved.")
#         return True
#     else:
#         print("Answer escalated!")
#         return False
import streamlit as st

# for streamlit
def human_review(answer):
    return


    # st.subheader("Human Review Required")
    # st.write("Suggested answer:")
    # st.write(answer)
    
    # approve = st.radio("Do you approve this answer?", ("Yes", "No"))
    # if approve == "Yes":
    #     return True
    # else:
    #     return False



import datetime

def log_llm_run(user_query, answer, docs, plan,is_high, log_file="llm_logs.txt"):
    current_time = datetime.datetime.now()

    log_entry = f"--- LLM Run: {current_time} ---\n"
    log_entry += f"User Query: {user_query}\n"
    log_entry += f"Collection Used: {plan}\n"
    log_entry += f"Confidence level: {is_high}\n"
    log_entry += f"Answer: {answer}\n"
    log_entry += "Sources Used:\n"
    for doc in docs:
        source_file = doc.metadata.get("source_file", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        log_entry += f"  - Source File: {source_file}, Chunk ID: {chunk_id}\n"

    log_entry += "\n\n"  # blank line at end for separation
    with open(log_file, "a") as file:
        file.write(log_entry)
    return log_entry



from langchain_community.llms import Cohere

from dotenv import load_dotenv
import os
load_dotenv()
cohere_api = os.getenv("COHERE_API_KEY")
llm = Cohere(cohere_api_key=cohere_api)

def run(user_query):
    plan = simple_planner(user_query)
    docs = get_retriever_docs(user_query, retriever_reports, retriever_stock)
    prompt = build_llm_prompt(docs, user_query)
    answer = llm(prompt)
    is_high = is_high_confidence(docs)
        
    log = log_llm_run(user_query,answer,docs,plan,is_high)
    
    return answer,log



