from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/pm", tags=["Preventive Maintenance"])

# Base PM task model
class PMTask(BaseModel):
    asset: str
    due_date: str  # e.g. "2025-05-10"

# For AI summarization
class PMNoteSummaryRequest(BaseModel):
    raw_notes: str
    priority: str = "balanced"  # controls model used (cost vs quality)

@router.get("/", response_model=List[PMTask])
def get_pm_schedule():
    return [
        {"asset": "Boiler A", "due_date": "2025-05-10"},
        {"asset": "Pump B", "due_date": "2025-05-12"}
    ]

@router.post("/", response_model=dict)
def add_pm_task(task: PMTask):
    return {"message": "PM task added", "data": task}

# 🔥 AI-Powered Summary for PM Notes
@router.post("/summarize-task", response_model=dict)
async def summarize_pm_notes(req: PMNoteSummaryRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = f"Summarize these maintenance notes into a clean, 1-2 sentence summary:\n\n{req.raw_notes}"
        result, cost, usage = await run_chat(model, "summarize", prompt)
        return {
            "summary": result.strip(),
            "model": model,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))