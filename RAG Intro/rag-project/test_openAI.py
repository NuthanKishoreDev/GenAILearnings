from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def test_openai():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for TechCorp RAG."},
            {"role": "user", "content": f"What is the Google Agentic AI Complete Learning Roadmap?"}
        ],
        temperature=0.7,
        max_tokens=512
    )

    print(f"Response: {response.choices[0].message.content}")
    
def query_openai(question, context):    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for TechCorp RAG."},
            {"role": "user", "content": f"Using the following context, answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"}
        ],
        temperature=0.7,
        max_tokens=5512
    )
    
    return response.choices[0].message.content