from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class DonutPanelType(Enum):
    Expediente = "Expediente"
    Requerimiento = "Requerimiento"
    Verificacion = "Verificacion"
    TareasPendientes = "TareasPendientes"

class DonutPanelRequest(BaseModel):
    DateIni: datetime = Field(..., description="Start date")
    DateEnd: datetime = Field(..., description="End date")
    Type: DonutPanelType = Field(..., description="Donut panel type")