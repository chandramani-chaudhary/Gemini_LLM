import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def gemini_llm(text):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text,
    )
    return response.text