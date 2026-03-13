import json
import numpy as np
import faiss

from src.embeddings import get_embedding

# Load dataset
with open("dataset/bfsi_150.json","r") as f:
    data=json.load(f)
questions=[item["input"] for item in data]

# Create embeddings
embeddings=[]
for q in questions:
    embeddings.append(get_embedding(q))
embeddings=np.array(embeddings).astype("float32")

# Create FAISS index
dimension=embeddings.shape[1]
index=faiss.IndexFlatL2(dimension)
index.add(embeddings)
def search_dataset(query):
    query_vector=get_embedding(query)
    query_vector=np.array([query_vector]).astype("float32")
    D,I=index.search(query_vector,1)
    if D[0][0] < 1.5:
        return data[I[0][0]]["output"]
    return None