from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/technicians", tags=["Technicians"])

class Technician(BaseModel):
    id: int
    name: str
    skills: List[str]

class TechSummaryRequest(BaseModel):
    technician_name: str
    recent_notes: str
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

@router.get("/", response_model=List[Technician])
def get_technicians():
    return [
        {"id": 1, "name": "John Doe", "skills": ["electrical", "hydraulics"]},
        {"id": 2, "name": "Maria Chavez", "skills": ["PLC", "pumps"]}
    ]

@router.post("/", response_model=dict)
def add_technician(tech: Technician):
    return {"message": "Technician added", "data": tech}

# 🔥 AI: Generate Technician Performance Summary
@router.post("/summary", response_model=dict)
async def summarize_technician(req: TechSummaryRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = (
            f"Write a professional performance summary for technician {req.technician_name} "
            f"based on the following work notes:\n\n{req.recent_notes}"
        )
        result, cost, usage = await run_chat(model, "review", prompt)
        return {
            "summary": result.strip(),
            "model": model,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))