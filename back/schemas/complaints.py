from pydantic import BaseModel
from datetime import datetime

class ComplaintSchema(BaseModel):
    id: str
    user_id: str
    date: datetime
    type: str
    description: str
    created_at: datetime
    updated_at: datetime

class ComplaintList(BaseModel):
    complaints: list[ComplaintSchema]