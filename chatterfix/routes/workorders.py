from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter()

# Pydantic models
class WorkOrder(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str = "open"
    assigned_to: Optional[str] = None
    due_date: Optional[str] = None
    equipment_id: Optional[str] = None
    downtime_minutes: Optional[int] = None
    parts_used: Optional[List[str]] = []
    images: Optional[List[str]] = []
    manuals: Optional[List[str]] = []
    logs: Optional[List[str]] = []

class WorkOrderCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "open"
    assigned_to: Optional[str] = None
    due_date: Optional[str] = None
    equipment_id: Optional[str] = None
    downtime_minutes: Optional[int] = None
    parts_used: Optional[List[str]] = []
    images: Optional[List[str]] = []
    manuals: Optional[List[str]] = []
    logs: Optional[List[str]] = []

# Root check
@router.get("/")
async def workorders_root():
    return {"message": "WorkOrders API is live"}

# Create a new work order
@router.post("/", response_model=WorkOrder, status_code=201)
async def create_workorder(workorder: WorkOrderCreate):
    workorder_id = str(uuid4())
    new_workorder = WorkOrder(id=workorder_id, **workorder.dict())
    db.collection("workorders").document(workorder_id).set(new_workorder.dict())
    return new_workorder

# Get all work orders
@router.get("/all", response_model=List[WorkOrder])
async def list_workorders():
    docs = db.collection("workorders").stream()
    return [WorkOrder(id=doc.id, **doc.to_dict()) for doc in docs]

# Get a single work order
@router.get("/{workorder_id}", response_model=WorkOrder)
async def get_workorder(workorder_id: str):
    doc = db.collection("workorders").document(workorder_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="WorkOrder not found")
    return WorkOrder(id=doc.id, **doc.to_dict())

# Update a work order
@router.put("/{workorder_id}", response_model=WorkOrder)
async def update_workorder(workorder_id: str, workorder_update: WorkOrderCreate):
    doc_ref = db.collection("workorders").document(workorder_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="WorkOrder not found")
    updated_data = {**doc.to_dict(), **workorder_update.dict()}
    doc_ref.set(updated_data)
    return WorkOrder(id=workorder_id, **updated_data)

# Delete a work order
@router.delete("/{workorder_id}")
async def delete_workorder(workorder_id: str):
    doc_ref = db.collection("workorders").document(workorder_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="WorkOrder not found")
    doc_ref.delete()
    return {"message": f"WorkOrder {workorder_id} deleted successfully"}