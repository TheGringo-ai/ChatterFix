from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from chatterfix.services.firestore_client import db

router = APIRouter()

class PM(BaseModel):
    id: str
    title: str
    frequency_days: int
    asset_id: str
    description: Optional[str] = None

class PMCreate(BaseModel):
    title: str
    frequency_days: int
    asset_id: str
    description: Optional[str] = None

# List All PMs
@router.get("/all", response_model=List[PM])
async def list_pms():
    docs = db.collection("pms").stream()
    return [PM(id=doc.id, **doc.to_dict()) for doc in docs]

# Get Single PM
@router.get("/{pm_id}", response_model=PM)
async def get_pm(pm_id: str):
    doc = db.collection("pms").document(pm_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="PM not found")
    return PM(id=doc.id, **doc.to_dict())

# Update PM
@router.put("/{pm_id}", response_model=PM)
async def update_pm(pm_id: str, pm_update: PMCreate):
    doc_ref = db.collection("pms").document(pm_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="PM not found")
    updated_data = {**doc.to_dict(), **pm_update.dict()}
    doc_ref.set(updated_data)
    return PM(id=pm_id, **updated_data)

# Delete PM
@router.delete("/{pm_id}")
async def delete_pm(pm_id: str):
    doc_ref = db.collection("pms").document(pm_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="PM not found")
    doc_ref.delete()
    return {"message": f"PM {pm_id} deleted successfully"}