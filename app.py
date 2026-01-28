from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI,UploadFile,Form
from resume_utils import extract_text
from ai_engine import analyze_resume

app = FastAPI()
@app.post("/analyze")
async def analyze(resume:UploadFile,job_desc:str = Form(...)):
    resume_text = extract_text(resume)
    analyze_result = analyze_resume(resume_text,job_desc)
    return {
        "status" : "success",
        "result" : analyze_result
    }