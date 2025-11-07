# rag_console.py
import os
from dotenv import load_dotenv
from indexer import load_pdf, split_text_paragraphs, create_chroma_db
from retriever import load_chroma_collection, get_relevant_passages
from generator import make_rag_prompt, generate_answer_from_prompt
import chromadb

load_dotenv()

CHROMA_PERSIST_PATH = "./chroma_persist"
COLLECTION_NAME = "rag_collection"
DATA_PATH = "C://GCP/GenAILearnings/RAG_With_Gemini/Data/WinWire Employee Handbook - India.pdf"


def initialize_index():
    """Index the PDF if ChromaDB does not exist."""
    if not os.path.exists(CHROMA_PERSIST_PATH):
        os.makedirs(CHROMA_PERSIST_PATH)
    chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_PATH)
    existing_collections = [c.name for c in chroma_client.list_collections()]
    if COLLECTION_NAME in existing_collections:
        print(f"[INFO] Collection '{COLLECTION_NAME}' already exists.")
        return

    print("[INFO] Creating new collection and indexing document...")
    text = load_pdf(DATA_PATH)
    chunks = split_text_paragraphs(text)
    print(f"[INFO] Split into {len(chunks)} chunks.")
    create_chroma_db(chunks, path=CHROMA_PERSIST_PATH, name=COLLECTION_NAME)
    print("[SUCCESS] Indexing complete.")


def main():
    """Main loop to handle user queries."""
    print("=== Gemini RAG Search Console ===")
    print("Type your question, or type 'exit' to quit.\n")

    # Ensure index exists
    initialize_index()

    db = load_chroma_collection(CHROMA_PERSIST_PATH, COLLECTION_NAME)

    while True:
        query = input("\n> Your Question: ").strip()
        if query.lower() in ["exit", "quit", "q"]:
            print("Exiting... Goodbye!")
            break
        if not query:
            continue

        print("\n[INFO] Retrieving relevant passages...")
        passages = get_relevant_passages(query, db, n_results=5)
        if not passages:
            print("[WARN] No relevant passages found.")
            continue

        print(f"[INFO] Retrieved {len(passages)} passages.")
        print("-" * 60)
        for i, p in enumerate(passages):
            print(f"[{i+1}] {p[:250]}{'...' if len(p) > 250 else ''}")
        print("-" * 60)

        prompt = make_rag_prompt(query, passages)
        print("[INFO] Generating answer using Gemini...\n")

        answer = generate_answer_from_prompt(prompt)
        print("=== ANSWER ===")
        print(answer)
        print("=" * 60)


if __name__ == "__main__":
    main()
    print("Gemini RAG Console is ready for queries.")