from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel

class SolicitudResponse(BaseModel):
    ID: int = Field(..., description="ID")
    Elemento: str = Field(..., description="Elemento")
    CaseNumber: int = Field(..., description="Case number")
    Cliente: str = Field(..., description="Cliente")
    Status: str = Field(..., description="Status")  # Assuming RegistroStatus is a string
    FechaRevision: Optional[datetime] = Field(None, description="Fecha revision")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")