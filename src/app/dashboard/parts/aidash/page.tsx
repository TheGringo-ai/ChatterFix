from fastapi import APIRouter, HTTPException
from fastapi import UploadFile, File
from pydantic import BaseModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/ai", tags=["AI"])

class SummaryRequest(BaseModel):
    notes: str

class CodeRequest(BaseModel):
    task: str
    context: str

class ImproveCodeRequest(BaseModel):
    existing_code: str
    goal: str

class AnalyzeCodeRequest(BaseModel):
    code: str

@router.post("/summarize")
async def summarize_notes(req: SummaryRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Summarize the following maintenance notes in a concise and technical tone."},
                {"role": "user", "content": req.notes}
            ],
            temperature=0.3
        )
        return {"summary": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# AI GENERATED CODE
@router.post("/review-file")
async def review_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Review the uploaded code for clarity, bugs, and refactor opportunities."},
                {"role": "user", "content": contents.decode("utf-8")}
            ]
        )
        return {"review": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# AI GENERATED CODE
class TestGenRequest(BaseModel):
    function_code: str

@router.post("/test-generator")
async def generate_tests(req: TestGenRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Write Pytest-based unit tests for the given function."},
                {"role": "user", "content": req.function_code}
            ]
        )
        return {
            "unit_tests": f"# AI GENERATED CODE\n{response.choices[0].message.content.strip()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# AI GENERATED CODE
class DocRequest(BaseModel):
    code: str

@router.post("/docstring")
async def add_docstring(req: DocRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Add proper Python docstrings to the following code."},
                {"role": "user", "content": req.code}
            ]
        )
        return {
            "docstringed_code": f"# AI GENERATED CODE\n{response.choices[0].message.content.strip()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-code")
async def generate_code_endpoint(req: CodeRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert developer. Generate high-quality, production-ready code based on the task and context."},
                {"role": "user", "content": f"Task: {req.task}\n\nContext:\n{req.context}"}
            ],
            temperature=0.2
        )
        return {
            "code": f"# AI GENERATED CODE\n{response.choices[0].message.content.strip()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/improve-code")
async def improve_code(req: ImproveCodeRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Improve the following code to meet the described goal. Optimize for clarity, maintainability, and performance."},
                {"role": "user", "content": f"Code:\n{req.existing_code}\n\nGoal:\n{req.goal}"}
            ],
            temperature=0.2
        )
        return {
            "improved_code": f"# AI GENERATED CODE\n{response.choices[0].message.content.strip()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-code")
async def analyze_code(req: AnalyzeCodeRequest):
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Analyze the following code for bugs, inefficiencies, and opportunities to refactor."},
                {"role": "user", "content": req.code}
            ],
            temperature=0.3
        )
        return {"analysis": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
