from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def rag_search(query):
    with open("rag_docs/banking_policy.txt") as f:
        text=f.read()

    splitter=CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs=splitter.split_text(text)
    embedding=HuggingFaceEmbeddings()
    db=Chroma.from_texts(docs,embedding)
    results=db.similarity_search(query,k=1)
    return results[0].page_content