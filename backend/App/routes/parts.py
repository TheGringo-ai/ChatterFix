from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/parts", tags=["Parts"])

class Part(BaseModel):
    id: int
    name: str
    location: str

class PartExplainRequest(BaseModel):
    part_name: str
    issue_context: str
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

@router.get("/", response_model=List[Part])
def get_parts():
    return [
        {"id": 3001, "name": "Seal Ring GSKT-4429", "location": "Bin A-12"},
        {"id": 3002, "name": "Bearing 6205Z", "location": "Bin B-3"}
    ]

@router.post("/", response_model=dict)
def add_part(part: Part):
    return {"message": "Part added", "data": part}

@router.post("/lookup-description", response_model=dict)
async def describe_part(req: PartExplainRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = (
            f"Explain the use and purpose of the part '{req.part_name}' in the following repair context:\n\n"
            f"{req.issue_context}"
        )
        result, cost, usage = await run_chat(model, "generate", prompt)
        return {
            "part_description": result.strip(),
            "model": model,
            "tokens_used": usage.model_dump() if hasattr(usage, "model_dump") else dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
