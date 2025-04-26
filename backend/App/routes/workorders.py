from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/workorders", tags=["Work Orders"])

# Basic WO data model
class WorkOrder(BaseModel):
    task: str

# AI Summarization Input
class WorkOrderSummaryRequest(BaseModel):
    raw_notes: str
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

# AI Description Generator Input
class TaskGenerationRequest(BaseModel):
    vague_issue: str
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

@router.get("/", response_model=List[WorkOrder])
def get_workorders():
    return [
        {"task": "Replace bearing"},
        {"task": "Lubricate gear motor"}
    ]

@router.post("/", response_model=dict)
def create_workorder(workorder: WorkOrder):
    return {"message": "Work order created", "data": workorder}

# 🔥 AI: Summarize Work Order Notes
@router.post("/summarize-notes", response_model=dict)
async def summarize_notes(req: WorkOrderSummaryRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = f"Summarize the following work order notes clearly and concisely:\n\n{req.raw_notes}"
        result, cost, usage = await run_chat(model, "summarize", prompt)
        return {
            "summary": result.strip(),
            "model": model,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔧 AI: Generate a Work Order Task Description
@router.post("/generate-task-description", response_model=dict)
async def generate_task_description(req: TaskGenerationRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = f"Based on this vague input, write a professional, clear work order task description:\n\n{req.vague_issue}"
        result, cost, usage = await run_chat(model, "generate", prompt)
        return {
            "task_description": result.strip(),
            "model": model,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))