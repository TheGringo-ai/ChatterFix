from fastapi import APIRouter

router = APIRouter()

@router.get("/parts")
def get_parts():
    return {"parts": ["Sample parts 1", "Sample parts 2"]}
