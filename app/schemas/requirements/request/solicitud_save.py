from pydantic import BaseModel, Field
from typing import List
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel

class SolicitudSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    IsAprobado: bool = Field(..., description="Is aprobado")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")