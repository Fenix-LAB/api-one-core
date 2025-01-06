from pydantic import BaseModel, Field
from datetime import datetime


class DateRequest(BaseModel):
    DateIni: datetime = Field(..., description="Start date in YYYY-MM-DD format")
    DateEnd: datetime = Field(..., description="End date in YYYY-MM-DD format")