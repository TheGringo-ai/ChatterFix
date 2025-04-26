from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Load OpenAI API key safely from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in environment variables.")

class SummarizeRequest(BaseModel):
    description: str

class TaskAssistantRequest(BaseModel):
    question: str

@router.post("/ai/summarize")
async def summarize_description(req: SummarizeRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Summarize this maintenance task clearly, concisely, and action-focused for a technician."},
                {"role": "user", "content": req.description}
            ]
        )
        summary = response['choices'][0]['message']['content']
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")

@router.post("/ai/task-assistant")
async def task_assistant(req: TaskAssistantRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a maintenance expert. Provide clear, step-by-step advice for technicians based on their question."},
                {"role": "user", "content": req.question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")

@router.get("/ai/ping")
async def ping():
    return {"status": "AI service online"}