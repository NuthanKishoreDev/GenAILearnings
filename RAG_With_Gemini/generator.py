# generator.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_KEY:
    raise ValueError("Set GOOGLE_API_KEY in environment or .env file")
genai.configure(api_key=GOOGLE_KEY)


def make_rag_prompt(query: str, relevant_passages: list) -> str:
    # join passages safely
    print("[DEBUG] Making RAG prompt...")
    print(f"[DEBUG] Relevant passages: {relevant_passages}")
    print(f"[DEBUG] User query: {query}")
    passage = " ".join([p.replace("'", "").replace('"', "").replace("\n", " ") for p in relevant_passages])
    prompt = (
    "You are a helpful and knowledgeable assistant. "
    "Use ONLY the information provided in the reference passage to answer the question. "
    "If the passage does not contain the answer, say politely that the information is not available. "
    "Provide a clear, well-structured answer in simple, natural language that a non-technical person can understand.\n\n"
    f"QUESTION: '{query}'\n\n"
    f"REFERENCE PASSAGE: '{passage}'\n\n"
    "ANSWER:")
    # prompt = (
    # "You are a helpful and knowledgeable assistant. "
    # "Use ONLY the information provided in the reference passage to answer the question. "
    # "Do NOT include any introductory statements such as 'Based on the passage' or 'Here is the answer'. "
    # "Start your answer directly with the content. "
    # "If the passage does not contain the answer, say politely that the information is not available. "
    # "Provide a clear, simple, and well-structured answer suitable for a non-technical audience.\n\n"
    # f"QUESTION: '{query}'\n\n"
    # f"REFERENCE PASSAGE: '{passage}'\n\n"
    # "ANSWER:"
    # )

    return prompt

def generate_answer_from_prompt(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    # article uses model.generate_content(prompt)
    # Example call per article:
    resp = model.generate_content(prompt,generation_config={"temperature":0.2})
    # resp.text is what article used
    # But client may return structure; fallback to str(resp)
    try:
        return resp.text
    except AttributeError:
        return str(resp)

if __name__ == "__main__":
    # quick example how you'd call it after retrieval
    from retriever import load_chroma_collection, get_relevant_passages
    db = load_chroma_collection(path="./chroma_persist", name="rag_collection")
    q = "What are Core Values?"
    passages = get_relevant_passages(q, db, n_results=3)
    prompt = make_rag_prompt(q, passages)
    ans = generate_answer_from_prompt(prompt)
    print("ANSWER:\n", ans)