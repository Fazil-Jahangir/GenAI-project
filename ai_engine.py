import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # <-- loads .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text,job_desc):
    prompt = f"""
    You are a resume expert.

    Resume Content:
    {resume_text}

    Job Description:
    {job_desc}

    Provide:
    1.Match percentage
    2.Missing skills
    3. Resume improvemenyt tips
    """

    response = client.chat.completions.create(model="gpt-5.2",
                                              messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content