from pydantic import BaseModel

class WorkOrder(BaseModel):
    id: str
    description: str
    status: str