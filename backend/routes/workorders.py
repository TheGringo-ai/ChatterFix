from fastapi import APIRouter

router = APIRouter()

@router.get("/workorders")
def get_work_orders():
    return {"message": "List of work orders"}