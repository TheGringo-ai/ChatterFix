from fastapi import APIRouter

router = APIRouter()

@router.get("/assets")
def get_assets():
    return {"assets": ["Sample assets 1", "Sample assets 2"]}
