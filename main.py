from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import google.generativeai as genai
import os
genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

while True : 
    question = input("Enter your question")
    response = chat.send_message(question)
    print(response.text)
    print("-------------")
