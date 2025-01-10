from pydantic import BaseModel, Field
from datetime import datetime

class SectionRequerimientosListRequest(BaseModel):
    DateIni: datetime = Field(..., description="Start date")
    DateEnd: datetime = Field(..., description="End date")