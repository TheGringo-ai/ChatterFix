from fastapi import APIRouter

router = APIRouter()

@router.get("/technician_logs")
def get_technician_logs():
    return {"technician_logs": ["Sample technician_logs 1", "Sample technician_logs 2"]}
