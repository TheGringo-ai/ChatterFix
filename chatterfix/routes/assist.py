from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from chatterfix.services.model_picker import pick_model
from chatterfix.services.openai_chat import run_chat

router = APIRouter(prefix="/assist", tags=["AI Assistant"])

class AssistRequest(BaseModel):
    task: str = Field(..., examples=["summarize", "review", "generate", "plan", "diagnose"])
    input: str = Field(..., description="Primary text or code input for AI to process")
    priority: str = Field("balanced", examples=["max", "balanced", "cost"])
    context: Optional[str] = Field(None, description="Optional additional context for more detailed responses")

@router.get("/")
async def assist_root():
    return {"message": "AI Assistant API is live"}

@router.post("/", response_model=dict)
async def assist(request: AssistRequest):
    """
    Processes a task through the selected AI model with optional additional context.
    """
    try:
        model = pick_model(request.task, request.priority)

        # Build the full prompt
        prompt = request.input
        if request.context:
            prompt = f"Context: {request.context}\n\nTask: {prompt}"

        result, cost, usage = await run_chat(model, request.task, prompt)
        
        return {
            "success": True,
            "model_used": model,
            "task": request.task,
            "priority": request.priority,
            "result": result,
            "tokens_used": dict(usage),
            "estimated_cost": f"${cost:.4f}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Assist failed: {str(e)}")