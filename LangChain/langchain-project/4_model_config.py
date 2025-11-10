import os
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Securely load API credentials
base_url = os.environ.get("OPENAI_API_BASE")
api_key = os.environ.get("OPENAI_API_KEY")

# Validate that credentials are set
if not base_url or not api_key:
    raise ValueError("OPENAI_API_BASE and OPENAI_API_KEY must be set")


# -------------------------------
# 1. Precise model for facts
# -------------------------------
precise_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0,     # Consistent, factual
    max_tokens=150
)

# -------------------------------
# 2. Creative model for stories
# -------------------------------
creative_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9,     # More creative
    max_tokens=200
)

# -------------------------------
# 3. Test prompt for both models
# -------------------------------
prompt = "Describe a rainbow"

print("=== PRECISE MODEL (temp=0) ===")
print(precise_model.invoke(prompt).content)

print("\n=== CREATIVE MODEL (temp=0.9) ===")
print(creative_model.invoke(prompt).content)

# -------------------------------
# 4. Streaming responses
# -------------------------------
streaming_model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    streaming=True       # Enable streaming mode
)

print("\n=== STREAMING RESPONSE ===")
for chunk in streaming_model.stream("Write a haiku about coding"):
    print(chunk.content, end="", flush=True)

print()  # new line after streaming output

# -------------------------------
# 5. Write success flag file
# -------------------------------
data_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(data_dir, exist_ok=True)
with open(os.path.join(data_dir, 'config-complete.txt'), 'w') as f:
    f.write("CONFIG_COMPLETE")
