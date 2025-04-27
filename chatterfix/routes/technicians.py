from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter()

# Pydantic models
class Technician(BaseModel):
    id: str
    name: str
    skills: List[str] = []
    certifications: List[str] = []
    photo_url: Optional[str] = None
    status: str = "active"

class TechnicianCreate(BaseModel):
    name: str
    skills: List[str] = []
    certifications: List[str] = []
    photo_url: Optional[str] = None
    status: str = "active"

# Root endpoint for technicians
@router.get("/")
async def technicians_root():
    return {"message": "Technicians API is live"}

# Create Technician
@router.post("/", response_model=Technician, status_code=201)
async def create_technician(technician: TechnicianCreate):
    tech_id = str(uuid4())
    new_technician = Technician(id=tech_id, **technician.dict())
    db.collection("technicians").document(tech_id).set(new_technician.dict())
    return new_technician

# List All Technicians
@router.get("/all", response_model=List[Technician])
async def list_technicians():
    docs = db.collection("technicians").stream()
    return [Technician(id=doc.id, **doc.to_dict()) for doc in docs]

# Get Single Technician
@router.get("/{tech_id}", response_model=Technician)
async def get_technician(tech_id: str):
    doc = db.collection("technicians").document(tech_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Technician not found")
    return Technician(id=doc.id, **doc.to_dict())

# Update Technician
@router.put("/{tech_id}", response_model=Technician)
async def update_technician(tech_id: str, technician_update: TechnicianCreate):
    doc_ref = db.collection("technicians").document(tech_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Technician not found")
    updated_data = {**doc.to_dict(), **technician_update.dict()}
    doc_ref.set(updated_data)
    return Technician(id=tech_id, **updated_data)

# Delete Technician
@router.delete("/{tech_id}")
async def delete_technician(tech_id: str):
    doc_ref = db.collection("technicians").document(tech_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Technician not found")
    doc_ref.delete()
    return {"message": f"Technician {tech_id} deleted successfully"}