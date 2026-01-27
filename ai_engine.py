import ollama

def analyze_resume(resume_text, job_desc):
    prompt = f"""
    You are a resume expert.
    
    Resume Content:
    {resume_text}

    Job Description:
    {job_desc}

    Provide:
    1. Match percentage
    2. Missing skills
    3. Resume improvement tips
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]