import os
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_classic.prompts import PromptTemplate

# Initialize model with proxy
model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    base_url=os.environ.get("OPENAI_API_BASE")
)

# Load HuggingFace embeddings (same as before)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# Create vector store from documents
print("📂 Creating vector store from documents...")
# Create sample documents directly
from langchain_core.documents import Document

sample_docs = [
    Document(page_content="LangChain is a framework for developing applications powered by language models."),
    Document(page_content="LCEL provides a declarative way to compose chains using the pipe operator."),
    Document(page_content="Memory systems in LangChain help maintain conversation context."),
    Document(page_content="RAG combines retrieval with generation for accurate, grounded responses."),
    Document(page_content="Best practice: Use chunk sizes of 500-1000 characters for optimal retrieval.")
]
documents = sample_docs
print(f"📄 Created {len(documents)} sample documents")

# Split documents
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create vector store
vectorstore = FAISS.from_documents(docs, embeddings)
print("✅ Vector store created!")

# Custom prompt for RAG
rag_prompt = PromptTemplate(
    template="""Use the following context to answer the question.
If you don't know the answer based on the context, say "I don't have that information."

Context: {context}

Question: {question}

Answer: """,
    input_variables=["context", "question"]
)

# Create retrieval chain
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",  # Stuff all docs into context
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 3}  # Retrieve top 3 chunks
    ),
    chain_type_kwargs={"prompt": rag_prompt},
    return_source_documents=True  # Return source docs for transparency
)

# Test the RAG system
test_questions = [
    "What is LCEL?",
    "What are the key features of LangChain?",
    "What is the recommended chunk size for documents?",
    "How do I use memory in LangChain?"
]

print("\n🤖 RAG System Test")
print("=" * 50)

for question in test_questions:
    print(f"\n❓ Question: {question}")
    result = qa_chain.invoke({"query": question})

    # Extract answer
    answer = result.get("result", "No answer found")
    print(f"💡 Answer: {answer}")

    # Show source documents
    source_docs = result.get("source_documents", [])
    if source_docs:
        print(f"📚 Sources ({len(source_docs)} chunks used):")
        for i, doc in enumerate(source_docs[:2], 1):
            print(f"   {i}. {doc.page_content[:60]}...")

with open('c://GCP//GenAILearnings//LangChain//langchain-project//data//retrieval-chain.txt', 'w') as f:
    f.write("RETRIEVAL_CHAIN_COMPLETE")