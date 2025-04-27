from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter()

# Pydantic models
class SummarizeRequest(BaseModel):
    description: str

class SummarizeResponse(BaseModel):
    summary: str
    id: Optional[str] = None  # Include ID for saved Firestore document

@router.get("/")
async def ai_root():
    return {"message": "AI Routes API is live"}

@router.post("/summarize", response_model=SummarizeResponse, status_code=201)
async def summarize_text(request: SummarizeRequest):
    """
    Summarizes the input description, saves to Firestore, and returns the summary.
    """
    cleaned_description = request.description.strip()
    if not cleaned_description:
        raise HTTPException(status_code=400, detail="Description cannot be empty.")

    summarized = (
        cleaned_description[:150] + "..." if len(cleaned_description) > 150 else cleaned_description
    )

    summary_id = str(uuid4())
    summary_record = {
        "id": summary_id,
        "original": cleaned_description,
        "summary": summarized
    }
    db.collection("summaries").document(summary_id).set(summary_record)

    return SummarizeResponse(id=summary_id, summary=summarized)