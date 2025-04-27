from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter()

# Pydantic models
class Part(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    asset_id: Optional[str] = None
    quantity: int = 0
    location: Optional[str] = None

class PartCreate(BaseModel):
    name: str
    description: Optional[str] = None
    asset_id: Optional[str] = None
    quantity: int = 0
    location: Optional[str] = None

# Root endpoint for parts
@router.get("/")
async def parts_root():
    return {"message": "Parts API is live"}

# Create Part
@router.post("/", response_model=Part, status_code=201)
async def create_part(part: PartCreate):
    part_id = str(uuid4())
    new_part = Part(id=part_id, **part.dict())
    db.collection("parts").document(part_id).set(new_part.dict())
    return new_part

# List All Parts
@router.get("/all", response_model=List[Part])
async def list_parts():
    docs = db.collection("parts").stream()
    return [Part(id=doc.id, **doc.to_dict()) for doc in docs]

# Get Single Part
@router.get("/{part_id}", response_model=Part)
async def get_part(part_id: str):
    doc = db.collection("parts").document(part_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Part not found")
    return Part(id=doc.id, **doc.to_dict())

# Update Part
@router.put("/{part_id}", response_model=Part)
async def update_part(part_id: str, part_update: PartCreate):
    doc_ref = db.collection("parts").document(part_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Part not found")
    updated_data = {**doc.to_dict(), **part_update.dict()}
    doc_ref.set(updated_data)
    return Part(id=part_id, **updated_data)

# Delete Part
@router.delete("/{part_id}")
async def delete_part(part_id: str):
    doc_ref = db.collection("parts").document(part_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Part not found")
    doc_ref.delete()
    return {"message": f"Part {part_id} deleted successfully"}