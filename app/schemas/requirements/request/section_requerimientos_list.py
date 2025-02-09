from pydantic import BaseModel, Field
from datetime import datetime

class SectionRequerimientosListRequest(BaseModel):
    dateIni: datetime = Field(..., description="Start date")
    dateEnd: datetime = Field(..., description="End date")