
import os

print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY", "❌ Not found"))
print("TEST_ENV_VAR:", os.getenv("TEST_ENV_VAR", "❌ Not found"))
