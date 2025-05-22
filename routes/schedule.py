from fastapi import APIRouter

router = APIRouter()

@router.get("/schedule")
def get_schedule():
    return {"schedule": ["Sample schedule 1", "Sample schedule 2"]}
