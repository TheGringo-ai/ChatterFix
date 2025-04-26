from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from App.services.model_picker import pick_model
from App.services.openai_chat import run_chat

router = APIRouter(prefix="/assist", tags=["AI Assistant"])

class AssistRequest(BaseModel):
    task: str = Field(..., examples=["summarize", "review", "generate"])
    input: str = Field(..., description="Text or code for AI to process")
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])

@router.post("/")
async def assist(request: AssistRequest):
    try:
        model = pick_model(request.task, request.priority)
        result, cost, usage = await run_chat(model, request.task, request.input)
        return {
            "model": model,
            "result": result,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))