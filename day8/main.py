import os
from time import sleep

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY not set. Add it to .env or your environment.")

client = Groq(api_key=my_api_key)
model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

JD = """
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME = """
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""


def ask_llm(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content


def step1_res_extract(resume):
    print("STEP 1")
    system_prompt = """
    You are a professional HR assistant. Extract the skills from the candidate's resume provided.
    Only return the skills, no other information. Do not invent any skills yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills, do not return any other filler information.
    """
    user_prompt = f"""
    Extract the skills from this resume
    {resume}
    """
    return ask_llm(system_prompt, user_prompt)


def step2_jd_extract(jd):
    print("STEP 2")
    system_prompt = """
    You are a professional HR assistant. Extract the skills from the job description provided.
    Only return the skills, no other information. Do not invent any skills yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills, do not return any other filler information.
    """
    user_prompt = f"""
    Extract the skills from this JD
    {jd}
    """
    return ask_llm(system_prompt, user_prompt)


def step3_match(candidate, jd):
    print("STEP 3")
    system_prompt = """
    You are a professional HR assistant. Compare the skills of the candidate and the skills required in the JD and produce a final score between 1 and 100.
    Also produce a short verdict whether the candidate is a good fit for the role.
    """
    user_prompt = f"""
    Compare and match the skills.
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)


if __name__ == "__main__":
    candidate = step1_res_extract(RESUME)
    print(candidate)
    sleep(2)

    jd = step2_jd_extract(JD)
    print(jd)
    sleep(2)

    score = step3_match(candidate, jd)
    print(score)
