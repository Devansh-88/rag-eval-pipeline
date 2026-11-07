
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

# Initialize Gemini client
client = genai.Client(
    api_key=api_key,
)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain RAG in 3 simple sentences."
)

# Print response
print("\nGemini Response:")
print(response.text)
