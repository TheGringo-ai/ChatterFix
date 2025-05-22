from fastapi import APIRouter

router = APIRouter()

@router.get("/workorders")
def get_workorders():
    return {
        "workorders": [
            {"id": 1, "title": "Replace filter", "status": "open"},
            {"id": 2, "title": "Fix broken pipe", "status": "in_progress"}
        ]
    }