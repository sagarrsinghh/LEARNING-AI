import os 
import sys
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

model = os.getenv("GROQ_MODEL")
if not model:
    raise ValueError("GROQ_MODEL environment variable is not set.")

client = Groq(api_key=my_api_key)

role = "user"

prompt = "DO you know about BANKAI?"

message = {
    "role": role,
    "content": prompt
}   
messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)
print(response.choices[0].message.content)
