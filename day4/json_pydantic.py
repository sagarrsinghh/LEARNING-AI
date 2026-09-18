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


#------------------------------------------------------------------
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    phone_number: str
    email: str
    issue: str

schema= Ticket.model_json_schema()

response_format={
    "type": "json_object",
}
system_prompt = f"""
extract the personal information from ticket strictly based on schema
and give me a JSON output.{schema}
"""
message_system= {
    "role": "system",
    "content": system_prompt
}

text = "Hello my name is Sagar . I have an Iphone 17 which is not working poroperly. My address is Jaipur and my phone number is 1351256643, My email is sgrrss11@gmail.com. " 
prompt = f"""This is a customer ticket. Please extract the personal information form this. 
{text} 
"""


# messgae me role and content
message = {
    "role": role,
    "content": prompt
}   
messages = [message_system, message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer = response.choices[0].message.content
print(answer)


# isko padhte kaise hai 

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

#inko pass kar sakte h 
print(f"\nName: {ticket.name}")
print(f"Phone Number: {ticket.phone_number}")
print(f"Email: {ticket.email}")
print(f"Issue: {ticket.issue}")

# overall use case is to extract the data from the text and convert it into a structured format using pydantic model. 
# This can be useful for automating the process of extracting information from customer tickets or other unstructured text data.

#LLM output ko structured kaise banaya jaye taaki dusre logo ko usse padh ne me or prase krne me asani ho.
