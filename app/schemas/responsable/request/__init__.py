from pydantic import BaseModel
from fastapi import Query

class ResponsableRequest(BaseModel):
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),