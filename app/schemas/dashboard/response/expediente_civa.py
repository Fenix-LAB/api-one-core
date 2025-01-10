from pydantic import BaseModel, Field
from datetime import datetime

class ExpedienteCivaResponse(BaseModel):
    Actualizacion: datetime = Field(..., description="Last update of the expediente civa")