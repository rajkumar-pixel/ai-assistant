AI Assistant Project

Objective:
Build a lightweight AI assistant for BFSI customer queries using dataset retrieval, small language model logic and RAG.

Architecture:

User Query
↓
Guardrails Check
↓
Dataset Similarity Search (FAISS)
↓
RAG Retrieval (Financial Knowledge)
↓
Fallback Response

Components:

Dataset Layer:
150 BFSI conversation samples in Alpaca format.

Similarity Layer:
SentenceTransformer embeddings with FAISS vector search.

RAG Layer:
Banking policy document retrieval using LangChain.

Guardrails:
Blocks sensitive data requests and non banking queries.

UI:
Streamlit interface for demo.

API:
FastAPI backend for testing.

Security Compliance:

No guessing of financial numbers
No personal data exposure
No OTP/password handling
Banking domain only responses

How to Run:

Install requirements:

pip install -r requirements.txt

Run UI:

streamlit run ui/streamlit_app.py

Run API:

uvicorn api:app --reload

Example Queries:

What is EMI
Loan interest rate
Payment failed
Account opening process

Future Improvements:

Fine tuning SLM
Larger dataset
Policy database expansion
Cloud deployment