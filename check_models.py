import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- RAW MODEL LIST ---")
try:
    # We remove all filters and just print the names
    for m in client.models.list():
        print(f"Model ID: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")