from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from uuid import UUID

class SolicitudResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    elemento: str = Field(..., description="Elemento")
    caseNumber: int = Field(..., description="Case number")
    cliente: str = Field(..., description="Cliente")
    status: int = Field(..., description="Status")  # Assuming RegistroStatus is a string
    fechaRevision: Optional[datetime] = Field(None, description="Fecha revision")
    areaRols: List[AreaRolModel] = Field(..., description="Area roles")
    responsables: List[ResponsableModel] = Field(..., description="Responsables")