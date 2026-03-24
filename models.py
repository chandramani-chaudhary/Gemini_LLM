import os
from google import genai

client = genai.Client(api_key="AIzaSyB5WlnkrbWcDfAX3D9EUJe2CjK3deGF79g")
def gemini_llm(text):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text,
    )
    return response.text