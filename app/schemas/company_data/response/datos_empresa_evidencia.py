from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.schemas.models.area_rol_model import AreaRolModel
from app.schemas.models.responsable_model import ResponsableModel
from app.schemas.models.hallazgo_option_model import HallazgoOptionModel

class DatosEmpresaEvidenciaResponse(BaseModel):
    ID: int = Field(..., description="ID")
    CaseNumber: int = Field(..., description="Case number")
    Fecha: Optional[datetime] = Field(None, description="Fecha")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")
    Recomendaciones: str = Field(..., description="Recomendaciones")
    Cliente: str = Field(..., description="Cliente")
    Hallazgo: HallazgoOptionModel = Field(..., description="Hallazgo")
    HallazgoComentarios: str = Field(..., description="Hallazgo comentarios")