from fastapi import APIRouter

router = APIRouter()

@router.get("/ai_console")
def get_ai_console():
    return {"ai_console": ["Sample ai_console 1", "Sample ai_console 2"]}
