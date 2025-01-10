from pydantic import BaseModel, Field
from datetime import datetime

class PaginationRequest(BaseModel):
    # Assuming PaginationRequest has some fields, add them here
    pass

class TareaResponsableRequest(PaginationRequest):
    DateIni: datetime = Field(..., description="Start date")
    DateEnd: datetime = Field(..., description="End date")