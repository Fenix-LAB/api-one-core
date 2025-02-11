from pydantic import BaseModel, Field
from typing import List
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from uuid import UUID

class SolicitudSaveRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    isAprobado: bool = Field(..., description="Is aprobado")
    areaRols: List[AreaRolModel] = Field(..., description="Area roles")
    responsables: List[ResponsableModel] = Field(..., description="Responsables")