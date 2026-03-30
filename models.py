import os
import google.generativeai as genai

import google.generativeai as genai

genai.configure(api_key="AIzaSyAx8SB6BDGDZnj1IQTs26JqBXQXqAnxyT8")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Hello")

print(response.text)