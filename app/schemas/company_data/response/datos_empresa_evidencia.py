from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.hallazgo_option import HallazgoOptionModel
from uuid import UUID

class DatosEmpresaEvidenciaResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    fecha: Optional[datetime] = Field(None, description="Fecha")
    areaRols: List[AreaRolModel] = Field(..., description="Area roles")
    responsables: List[ResponsableModel] = Field(..., description="Responsables")
    recomendaciones: str = Field(..., description="Recomendaciones")
    rliente: str = Field(..., description="Cliente")
    hallazgo: HallazgoOptionModel = Field(..., description="Hallazgo")
    hallazgoComentarios: str = Field(..., description="Hallazgo comentarios")