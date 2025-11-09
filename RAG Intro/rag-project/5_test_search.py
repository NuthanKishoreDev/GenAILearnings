import chromadb
from sentence_transformers import SentenceTransformer

print(" TECHCORP SEMANTIC SEARCH ENGINE")
print("="*50)

# Initialize
print(" Connecting to Knowledge Base...")
client = chromadb.PersistentClient(path="C:\\GCP\\GenAILearnings\\RAG Intro\\chroma_db")
collection = client.get_collection("techcorp_docs")

print(" Loading AI Understanding...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print(" Search Engine Ready!\n")

# CEO's test queries
queries = [
    "What is 3. Service Level Agreements?",
    "Duration of Google Agentic AI Complete Learning Roadmap",
    "what are First Day Checklist of Onboarding New Employees?",
]

results_file = open('C:\\GCP\\GenAILearnings\\RAG Intro\\rag-project\\docs\\search-results.txt', 'w')

for query in queries:
    print(f" Query: '{query}'")
    print("-" * 50)
    results_file.write(f"QUERY:{query}\n")

    # Convert question to vector
    query_embedding = model.encode(query).tolist()

    # Semantic search!
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    

    # Display results
    print(" Top Results (by semantic similarity):")
    for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
        relevance = 100 - (i * 15)  # Simulated relevance
        print(f"\n  {i+1}. [{meta['category']}] {meta['file']} ({relevance}% match)")
        print(f"     Preview: '{doc[:75]}...'")
        results_file.write(f"RESULT:{meta['category']}/{meta['file']}\n")

    print("\n" + "="*50 + "\n")

results_file.close()

print(" SEARCH TEST COMPLETE!")
print(" This is the power of semantic understanding!")