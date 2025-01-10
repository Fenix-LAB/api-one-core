from pydantic import BaseModel, Field
from app.schemas.models.area_rol import AreaRolType
from enum import Enum

class RiesgoTarea(Enum):
    Alto = "Alto"
    Medio = "Medio"
    Bajo = "Bajo"

class TareaResponsableResponse(BaseModel):
    Area: AreaRolType = Field(..., description="Area rol type")
    Usuario: str = Field(..., description="Usuario")
    Asignadas: int = Field(..., description="Asignadas")
    Completadas: int = Field(..., description="Completadas")
    RiegoCode: RiesgoTarea = Field(..., description="Riesgo tarea code")