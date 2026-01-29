from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
google_gemini_api_key = os.getenv("GOOGLE_API_KEY")     # Enter your GOOGLE GEMINI API KEY here

client = OpenAI(
    api_key = google_gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat_agent(prompt):
    response = client.chat.completions.create(
        model="models/gemini-2.5-flash",
        messages=[
            {'role':'system', 'content':"You are a helpful assistant"},
            {'role':'user', 'content':prompt}
        ]
    )
    return response.choices[0].message.content

input_prompt = input("> ")
print(chat_agent(input_prompt))