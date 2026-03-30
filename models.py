import os
from google import genai

client = genai.Client(api_key="AIzaSyB2-x303ZdbmYGtXtgeIFtH8vcim3AC1PU")
def gemini_llm(text):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text,
    )
    return response.text