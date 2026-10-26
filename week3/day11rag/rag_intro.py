import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not set. Add it to .env or your shell environment.")

client = Groq(api_key=my_api_key)
model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

knowledge_base = {
    "age": "The age of Pratyush is 25 years.",
    "net worth": "The net worth of Pratyush is 2000.",
}


def retrieve_info(question):
    q = question.lower()
    if "age" in q:
        return knowledge_base["age"]
    if "net worth" in q:
        return knowledge_base["net worth"]
    return "No relevant information found in the knowledge base."


def ask_llm(question):
    context = retrieve_info(question)

    system_prompt = (
        "Answer in one line only. Answer only based on this context. "
        f"Do not hallucinate. Context: {context}"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


question = "What is Pratyush's age?"
print(ask_llm(question))
