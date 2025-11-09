import os
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

print("TECHCORP KNOWLEDGE INGESTION SYSTEM")
print("="*50)

# Initialize systems
print("Connecting to AI Brain (from Task 3)...")
client = chromadb.PersistentClient(path="C:\\GCP\\GenAILearnings\\RAG Intro\\chroma_db")
collection = client.get_collection("techcorp_docs")

print("Loading Semantic Processor (from Task 5)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("All systems online!\n")

# Process documents
print("Beginning knowledge transfer...")
doc_count = 0
total_chunks = 0

# 🔹 Updated: Read all files directly from the folder (no subdirectory iteration)
repo_path = Path('C:\\GCP\\GenAILearnings\\RAG Intro\\rag-project\\Knowledge_Repository')

for doc in repo_path.glob('*.*'):
    print(f"Processing {doc.name}", end="")
    with open(doc, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Apply chunking strategy from Task 4!
    chunks = [content[i:i+500] for i in range(0, len(content), 400)]

    for i, chunk in enumerate(chunks):
        doc_id = f"{doc.stem}_{i}"
        # Apply embedding from Task 5!
        embedding = model.encode(chunk).tolist()

        # Store in database from Task 3!
        collection.add(
            ids=[doc_id],
            embeddings=[embedding],
            documents=[chunk],
            metadatas={"file": doc.name, "category": "Knowledge_Repository"}
        )
        total_chunks += 1

    doc_count += 1
    print(f" ({len(chunks)} chunks)")

print("\n" + "="*50)
print(f"INGESTION COMPLETE!")
print(f"Statistics:")
print(f"   • Documents processed: {doc_count}")
print(f"   • Knowledge chunks: {total_chunks}")
print(f"   • AI IQ increased: +{doc_count*10} points")

# Save results
with open('C:\\GCP\\GenAILearnings\\RAG Intro\\rag-project\\docs\\ingest-complete.txt', 'w') as f:
    f.write(f"DOCS:{doc_count},CHUNKS:{collection.count()}")
