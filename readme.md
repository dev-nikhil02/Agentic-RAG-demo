# Agentic-RAG-demo

## About
Agentic RAG demo is a demonstration project showcasing Retrieval Augmented Generation (RAG) in an agentic framework.  
The project illustrates how to combine retrieval mechanisms with generative models to enable more informed and context-aware AI agents.

This repository contains both Jupyter Notebooks and a Streamlit web application, demonstrating the concepts, architecture, and applications of RAG. The project is specifically customized for Google financial data (2023 and 2024) and Google stock price analysis.

## Project Phases

### 1. Research & Data Preparation
- **Data Collection:** Gathered Google financial reports, news, and stock price data for 2023 and 2024.
- **Preprocessing:** Cleaned and structured the data for efficient retrieval and downstream tasks.
- **Exploration:** Analyzed the data to identify key financial indicators and trends relevant to Google.

### 2. Jupyter Notebook Prototyping
- **Step-by-step RAG Implementation:** Developed and tested the RAG pipeline in Jupyter Notebooks for rapid experimentation.
- **Modular Design:** Built retriever and generator modules with clear interfaces for easy extension.
- **Evaluation:** Assessed the quality of retrieval and generation on Google financial queries.

### 3. Streamlit Application
- **Interactive UI:** Built a user-friendly Streamlit web app for real-time querying and visualization.
- **Custom Features:** Added options to select between different types of Google financial data (e.g., quarterly reports, stock prices).
- **Visualization:** Integrated charts for Google stock price trends and financial metrics.
- **Logs:** Displayed logs and intermediate results for transparency and debugging.

## Features
- Integration of retrieval and generation models for enhanced performance
- Step-by-step implementation in Jupyter Notebooks
- Streamlit UI for interactive exploration and visualization
- Modular architecture for easy experimentation and extension
- Example use cases and scenarios for retrieval-augmented agents
- Customization for Google financial data (2023, 2024) and stock price analysis

## Installation Guide

### Prerequisites
- Python 3.10 or higher
- Jupyter Notebook or JupyterLab environment
- Streamlit
- Git (to clone the repository)

### Step 1: Clone the repository
```bash
git clone https://github.com/dev-nikhil02/Agentic-RAG-demo
cd Agentic-RAG-demo
```

### Step 2: Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Set API Keys (if required)
Set your Cohere API key in your environment or in a `.env` file:
```
COHERE_API_KEY=your_api_key
```

### Step 4: Install dependencies
You can install the required Python packages by running:
```bash
pip install -r requirements.txt
```

## Architecture Overview

The project architecture is designed around two main components:

1. **Retriever Module:**  
   - Searches and retrieves relevant documents or passages from the Google financial dataset based on input queries.
   - Uses vector similarity search (e.g., ChromaDB) for efficient retrieval.

2. **Generator Module:**  
   - Uses retrieved documents as context to generate informed responses or summaries.
   - Powered by generative transformer models (e.g., T5, GPT).

3. **Streamlit UI Layer:**  
   - Provides an interactive interface for users to input queries, select data types (financial reports, stock prices), and view results.
   - Visualizes Google stock price trends and financial metrics.

**Customized RAG Pipeline for Google Financial Data:**
- Data Source: Google financial reports (2023, 2024), stock price CSVs.
- Retrieval: Semantic search over financial documents and time-series data.
- Generation: Summarization and Q&A tailored to financial context.
- Stored Logs for all of this.
### Architectural Diagram
![Architecture Diagram](jpeg/architecture_screenshot.png)  
*Customized for Google financial data and stock price analysis.*

## Usage

### Running the research Notebooks
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open the main notebook file (e.g., `Agentic-RAG-demo.ipynb`).
3. Follow the notebook cells step by step:
   - Load the Google financial dataset (2023, 2024)
   - Initialize the retriever model
   - Initialize the generator model
   - Run the RAG pipeline with sample queries (e.g., "What was Google's revenue in Q2 2023?")
   - Visualize stock price trends and financial summaries

### Running the Streamlit App
Use this command in your terminal after installing the dependencies. This will run the app in your browser:
```bash
streamlit run app.py
```
**Streamlit UI Features:**
- Query input for financial questions about Google
- Dropdown to select data type (financial report, stock price)
- Display of generated answers with retrieved context
- Interactive charts for Google stock price (2023, 2024)
- Logs and intermediate results for transparency

## Screenshots / Results

### Sample Output
> ![Sample Output](jpeg/answer.png)  
> *Example of generated text with retrieved context for Google financial data.*

### Notebook Interface
> ![Notebook Screenshot](jpeg/main_ipynb.png)  
> *Interactive Jupyter Notebook demonstrating the workflow.*

### Logs File
> ![logs file](jpeg/logs.png)  
> *Stored logs in separate file.*

### Streamlit UI
> ![Streamlit Screenshot](jpeg/UI.png)  
> *Streamlit app interface for querying Google financial data and visualizing stock prices.*

## Contributing
Contributions, suggestions, and bug reports are welcome! Please open an issue or submit pull requests to improve the project.

---
