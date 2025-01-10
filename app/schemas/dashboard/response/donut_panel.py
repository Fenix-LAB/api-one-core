from pydantic import BaseModel, Field
from enum import Enum

class DonutPanelCode(Enum):
    Green = "Green"
    Red = "Red"
    Orange = "Orange"

class DonutPanelStatus(Enum):
    Completado = "Completado"
    Pendiente = "Pendiente"
    Hallazgos = "Hallazgos"
    Bajo = "Bajo"
    Medio = "Medio"

class DonutPanelResponse(BaseModel):
    Porcentaje: float = Field(..., description="Porcentaje")
    Cantidad: int = Field(..., description="Cantidad")