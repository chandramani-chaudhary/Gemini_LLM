import os
from google import genai

client = genai.Client(api_key="AIzaSyDxlyeAkcETMHL60NZjoFjyaN56gjqNZmM")
def gemini_llm(text):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text,
    )
    return response.text