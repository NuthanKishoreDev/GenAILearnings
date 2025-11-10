import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create sample documents directly (self-contained)
sample_texts = [
    """LangChain is a framework for developing applications powered by language models.
    It provides tools to connect LLMs with external data sources and other tools.""",

    """LCEL (LangChain Expression Language) uses the pipe operator to chain components.
    Example: prompt | model | output_parser creates a simple chain.""",

    """Memory in LangChain allows conversations to maintain context across interactions.
    ConversationBufferMemory stores the entire conversation history.""",

    """RAG (Retrieval Augmented Generation) combines document retrieval with LLM generation.
    It helps ground AI responses in factual, domain-specific knowledge.""",

    """Vector stores like FAISS enable semantic search over document embeddings.
    They convert text to vectors and find similar content based on meaning."""
]

# Convert to Document objects
documents = [Document(page_content=text) for text in sample_texts]
print(f"📄 Created {len(documents)} sample documents")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

print(f"📚 Processing {len(chunks)} document chunks...")

# Create HuggingFace embeddings - NO API KEY REQUIRED!
print("\n🤗 Loading HuggingFace embeddings (free, no API key needed)...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},  # Use 'cuda' if GPU available
    encode_kwargs={'normalize_embeddings': True}  # For better similarity search
)

print("   Model: all-MiniLM-L6-v2 (fast and efficient)")
print("   Embedding dimension: 384")
print("   ✅ Ready to embed documents!")

# Create FAISS vector store (in-memory, no external DB needed)
print("\n🔨 Creating FAISS vector store...")
vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("✅ Vector store created successfully!")
print("   Type: FAISS (Facebook AI Similarity Search)")
print("   Storage: In-memory (fast!)")

# Save vector store for later use
vectorstore.save_local("c://GCP//GenAILearnings//LangChain//langchain-project//data//vectorstore//faiss_index")
print("   💾 Saved to: .data//vectorstore//faiss_index")

# Test similarity search
query = "What is LCEL?"
print(f"\n🔍 Testing search for: '{query}'")

results = vectorstore.similarity_search(query, k=2)
print(f"\n📊 Found {len(results)} relevant chunks:")
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(f"   {doc.page_content}")
    print(f"   {doc.page_content[:100]}...")

# Test with similarity scores
print("\n📏 Search with similarity scores:")
results_with_scores = vectorstore.similarity_search_with_score(query, k=2)
for i, (doc, score) in enumerate(results_with_scores, 1):
    print(f"\nResult {i} (score: {score:.4f}):")
    print(f"   {doc.page_content}")
    print(f"   {doc.page_content[:100]}...")

with open('c://GCP//GenAILearnings//LangChain//langchain-project//data//vector-store.txt', 'w') as f:
    f.write("VECTOR_STORE_COMPLETE")