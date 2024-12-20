from tkinter import *
from tkinter import scrolledtext

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import google.generativeai as genai
import os
genai.configure(api_key=os.environ['API_KEY'])
import time
from threading import Thread

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)


root = Tk()
root.geometry("500x500")
root.title("ChatBot")

def send():
    question = questionEntry.get()
    response = chat.send_message(question, stream=True)
    for chunk in response : 
        responseText.insert(END, chunk.text)
        responseText.see(END)
    questionEntry.delete(0, END)

def sendStream():
    t = Thread(target=send)
    t.start()
   
titleText = Label(root, text="ChatBot")
titleText.pack()

responseText = scrolledtext.ScrolledText(root)
responseText.pack()

questionEntry = Entry(root, width=80)
questionEntry.pack()

sendButton = Button(root , text="Send" , command=sendStream)
sendButton.pack()



root.mainloop()