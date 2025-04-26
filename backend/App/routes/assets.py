from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/assets", tags=["Assets"])

class Asset(BaseModel):
    id: int
    name: str

class InspectionGenRequest(BaseModel):
    asset_name: str = Field(..., example="Pump A")
    known_issues: str = Field(..., example="Recently overheating, minor leaks")
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

@router.get("/", response_model=List[Asset])
def get_assets():
    return [
        {"id": 101, "name": "Conveyor Belt A"},
        {"id": 102, "name": "Packaging Robot"}
    ]

@router.post("/", response_model=dict)
def create_asset(asset: Asset):
    return {"message": "Asset added", "data": asset}

# 🔍 AI-Generated Inspection Plan
@router.post("/generate-inspection", response_model=dict)
async def generate_inspection(req: InspectionGenRequest):
    try:
        model = "gpt-4.1-mini" if req.priority != "max" else "gpt-4o"
        prompt = (
            f"Generate a maintenance inspection checklist for asset '{req.asset_name}' "
            f"that is experiencing: {req.known_issues}.\n\n"
            "Return clear, bullet-pointed tasks suitable for a technician."
        )
        result, cost, usage = await run_chat(model, "generate", prompt)
        return {
            "inspection_steps": result.strip(),
            "model": model,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))