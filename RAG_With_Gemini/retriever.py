# retriever.py
import os
import chromadb
from indexer import GeminiEmbeddingFunction
from dotenv import load_dotenv
load_dotenv()

def load_chroma_collection(path: str, name: str):
    chroma_client = chromadb.PersistentClient(path=path)
    collection = chroma_client.get_collection(name=name, embedding_function=GeminiEmbeddingFunction())
    return collection

def get_relevant_passages(query: str, collection, n_results: int = 5):
    # article uses db.query(query_texts=[query], n_results=n_results)['documents'][0]
    resp = collection.query(query_texts=[query], n_results=n_results)
    # resp has 'documents' key: list of lists (for batch queries)
    docs = resp.get("documents", [])
    if len(docs) > 0:
        return docs[0]   # list of retrieved passages
    return []

if __name__ == "__main__":
    CHROMA_PERSIST_PATH = r"./chroma_persist"
    COLLECTION_NAME = "rag_collection"
    db = load_chroma_collection(CHROMA_PERSIST_PATH, COLLECTION_NAME)
    q = "What are Core Values?"
    hits = get_relevant_passages(q, db, n_results=5)
    print("Top passages:")
    for i, h in enumerate(hits):
        print(f"--- Passage {i} ---\n{h}\n")