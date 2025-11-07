import os
import re
from typing import List
from pypdf import PdfReader
import chromadb
from chromadb import Documents, EmbeddingFunction
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_KEY:
    raise ValueError("Set GOOGLE_API_KEY in environment or .env file")
genai.configure(api_key=GOOGLE_KEY)

# 1) PDF loader
def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n\n"
    return text

# 2) simple paragraph splitter (as in article)
def split_text_paragraphs(text: str) -> List[str]:
    # split by double newline or newline newline variants
    parts = re.split(r'\n\s*\n', text)
    return [p.strip() for p in parts if p.strip()]

# 3) Gemini embedding function class for Chroma
class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents):
        # uses same model name shown in the article
        model = "models/embedding-001"
        # genai.embed_content returns a dict; article uses task_type "retrieval_document"
        resp = genai.embed_content(model=model, content=input, task_type="retrieval_document", title="Custom Embedding")
        # resp structure per article: ["embedding"] or similar; adapt to client output shape
        # genai embed_content can return {"embedding": ...} or list — we'll try to return resp["embedding"]
        if isinstance(resp, dict) and "embedding" in resp:
            return resp["embedding"]
        # fallback if output differs:
        return resp

def create_chroma_db(documents: List[str], path: str, name: str):
    chroma_client = chromadb.PersistentClient(path=path)
    # create collection (embedding_function is an instance)
    collection = chroma_client.create_collection(name=name, embedding_function=GeminiEmbeddingFunction())
    ids=[]
    for i, doc in enumerate(documents):
        collection.add(documents=[doc], ids=[str(i)])
        ids.append(str(i))
    return collection

if __name__ == "__main__":
    # configure
    DATA_PATH = r"./data/your_docs.pdf"   # change to your file(s)
    CHROMA_PERSIST_PATH = r"./chroma_persist"  # directory to persist DB
    COLLECTION_NAME = "rag_collection"

    text = load_pdf(DATA_PATH)
    chunks = split_text_paragraphs(text)
    print(f"Loaded and split into {len(chunks)} chunks")

    db = create_chroma_db(chunks, path=CHROMA_PERSIST_PATH, name=COLLECTION_NAME)
    print("Indexing complete. Collection created:", COLLECTION_NAME)
