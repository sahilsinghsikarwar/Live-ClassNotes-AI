
from pathlib import Path
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in backend/.env")

print("Connecting to Gemini...", flush=True)

# Initialize Gemini client
client = genai.Client(
    api_key=api_key,
    http_options={"timeout": 30000}
)

try:
    response = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input="Write a short welcome message for a classroom."
    )

    print("\nGemini API Working Successfully!")
    print("\nAI Response:")
    print(response.output_text)

except Exception as e:
    print("\nGemini API Error:")
    print(repr(e))
