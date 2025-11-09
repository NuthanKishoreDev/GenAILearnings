import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os
import test_openAI
load_dotenv()
print(" TECHCORP RAG PIPELINE TEST")
print("="*50)

# Initialize all systems
print(" Initializing RAG Components...")
client = chromadb.PersistentClient(path="c://GCP//GenAILearnings//RAG Intro//chroma_db")
collection = client.get_collection("techcorp_docs")
model = SentenceTransformer('all-MiniLM-L6-v2')
print(" All systems operational!\n")

def test_rag_pipeline(question):
    """Test the complete RAG Pipeline"""

    print(f" Question: '{question}'")
    print("-" * 50)

    # 1. RETRIEVAL PHASE
    print("\n PHASE 1: RETRIEVAL")
    print("  Converting question to vector...")
    query_embedding = model.encode(question).tolist()
    print("  Searching knowledge base...")

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print(f"   Found {len(results['documents'][0])} relevant documents!")
    
    # 2. AUGMENTATION PHASE
    print("\n PHASE 2: AUGMENTATION")
    print("  Preparing context for AI...")
    context = "\n\n".join(results['documents'][0])

    # 3. GENERATION PHASE (Simulated)
    print("\n PHASE 3: GENERATION")
    print("  AI processing with context...")

    # Simulated response using OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = test_openAI.query_openai(
        question=question,
        context=context
    )
    
    print("   Response generated!")

    return {
        'question': question,
        'sources_used': len(results['documents'][0]),
        'answer': response.choices[0].message.content
    }


def main():
    # Test the pipeline
    print("\n" + "="*50)
    print(" TESTING COMPLETE PIPELINE")
    print("="*50)

    # test_question = "Any Holiday on 25-Dec-25 in winwire?"
    while True:
        test_question = input("Enter your test question for the RAG pipeline: ")
        result = test_rag_pipeline(test_question)
        print("\n" + "="*50)
        print(" PIPELINE RESULTS")
        print("="*50)
        print(f" Question: {result['question']}")
        print(f" Sources Used: {result['sources_used']} documents")
        print(f" Answer: {result['answer']}")


        # Save pipeline verification
        with open('C:\\GCP\\GenAILearnings\\RAG Intro\\rag-project\\docs\\rag-pipeline-test.txt', 'w') as f:
            f.write(f"PIPELINE:COMPLETE,SOURCES:{result['sources_used']}")

        print("\n" + "="*50)
        print(" SUCCESS! RAG Pipeline Working!")
        print("="*50)
    
if __name__ == "__main__":
    main()
    print(" RAG Pipeline Test Completed!")