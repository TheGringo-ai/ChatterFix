from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from chatterfix.services.firestore_client import db

router = APIRouter()

# Pydantic models
class Asset(BaseModel):
    id: str
    name: str
    location: Optional[str] = None
    status: str = "active"

class AssetCreate(BaseModel):
    name: str
    location: Optional[str] = None
    status: str = "active"

# Root endpoint for assets
@router.get("/")
async def assets_root():
    return {"message": "Assets API is live"}

# Create Asset
@router.post("/", response_model=Asset, status_code=201)
async def create_asset(asset: AssetCreate):
    asset_id = str(uuid4())
    new_asset = Asset(id=asset_id, **asset.dict())
    db.collection("assets").document(asset_id).set(new_asset.dict())
    return new_asset

# List All Assets
@router.get("/all", response_model=List[Asset])
async def list_assets():
    docs = db.collection("assets").stream()
    return [Asset(id=doc.id, **doc.to_dict()) for doc in docs]

# Get Single Asset
@router.get("/{asset_id}", response_model=Asset)
async def get_asset(asset_id: str):
    doc = db.collection("assets").document(asset_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Asset not found")
    return Asset(id=doc.id, **doc.to_dict())

# Update Asset
@router.put("/{asset_id}", response_model=Asset)
async def update_asset(asset_id: str, asset_update: AssetCreate):
    doc_ref = db.collection("assets").document(asset_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Asset not found")
    updated_data = {**doc.to_dict(), **asset_update.dict()}
    doc_ref.set(updated_data)
    return Asset(id=asset_id, **updated_data)

# Delete Asset
@router.delete("/{asset_id}")
async def delete_asset(asset_id: str):
    doc_ref = db.collection("assets").document(asset_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Asset not found")
    doc_ref.delete()
    return {"message": f"Asset {asset_id} deleted successfully"}