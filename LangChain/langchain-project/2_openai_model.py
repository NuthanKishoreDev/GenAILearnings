import os,dotenv
dotenv.load_dotenv()

from langchain_openai.chat_models import ChatOpenAI


# OPENAI_API_KEY must already be set in environment
# example: export OPENAI_API_KEY="your_key"

# Initialize model
model = ChatOpenAI(
    model="gpt-4.1-mini",   # ✅ Correct model name
    temperature=0,
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Test #1
response = model.invoke("Hello! What's 2+2?")
print("User: Hello! What's 2+2?")
print("AI:", response.content)

# Test #2
response = model.invoke("What's the capital of France?")
print("\nUser: What's the capital of France?")
print("AI:", response.content)

# Save progress
with open('C://GCP//GenAILearnings//LangChain//langchain-project//data/first-model.txt', 'w') as f:
    f.write("FIRST_MODEL_COMPLETE")
