from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter(
    prefix="/review",
    tags=["Review"],
)

# Pydantic models
class ReviewItem(BaseModel):
    workorder_id: int
    asset: str
    status: str = "Pending"

class ReviewAction(BaseModel):
    reason: str

# Root confirmation endpoint
@router.get("/")
async def review_root():
    return {"message": "Review API is live"}

# Fetch list of work orders pending review
@router.get("/pending", response_model=List[ReviewItem])
async def get_pending_reviews():
    docs = db.collection("reviews").stream()
    return [ReviewItem(**doc.to_dict()) for doc in docs]

# Approve a specific work order
@router.post("/approve/{workorder_id}")
async def approve_workorder(workorder_id: int):
    docs = db.collection("reviews").where("workorder_id", "==", workorder_id).stream()
    found = False
    for doc in docs:
        db.collection("reviews").document(doc.id).delete()
        found = True
    if not found:
        raise HTTPException(status_code=404, detail="Work order not found for approval.")
    return {"message": f"Work order {workorder_id} approved successfully."}

# Reject a specific work order
@router.post("/reject/{workorder_id}")
async def reject_workorder(workorder_id: int, action: ReviewAction):
    docs = db.collection("reviews").where("workorder_id", "==", workorder_id).stream()
    found = False
    for doc in docs:
        db.collection("reviews").document(doc.id).update({
            "status": f"Rejected: {action.reason}"
        })
        found = True
    if not found:
        raise HTTPException(status_code=404, detail="Work order not found for rejection.")
    return {"message": f"Work order {workorder_id} rejected.", "reason": action.reason}