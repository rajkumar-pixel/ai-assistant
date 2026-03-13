from fastapi import FastAPI
from src.assistant import assistant
app=FastAPI()
@app.get("/ask")
def ask(query:str):
    response=assistant(query)
    return {"response":response}