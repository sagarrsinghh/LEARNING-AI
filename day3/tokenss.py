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
prompt1 = "hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write 1000 words essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
            "role": role,
            "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(
        model=model,    
    messages=messages,
    max_tokens=100
    )       
    usage = response.usage
    print(f"Prompt: {prompt}--> your_token: {usage.prompt_tokens}, completion_token: {usage.completion_tokens}, total_token: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}" )

# message = {
#    "role": role,
#    "content": prompt
# }   
# messages = [message]
#
# response = client.chat.completions.create(    
#    model=model,
#    messages=messages,
# )
# print(response.choices[0].message.content)
