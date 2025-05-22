from pydantic import BaseModel
from typing import Optional

class WorkOrder(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    status: str
    asset_id: str
    priority: str
    technician: str
