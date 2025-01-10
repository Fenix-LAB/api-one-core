from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.file_info import FileInfoModel

class RequerimientosEvidenciaResponse(BaseModel):
    ID: int = Field(..., description="ID")
    Elemento: str = Field(..., description="Elemento")
    CaseNumber: int = Field(..., description="Case number")
    Status: str = Field(..., description="Status")  # Assuming RegistroStatus is a string
    FechaInicio: Optional[datetime] = Field(None, description="Fecha inicio")
    FechaVencimiento: Optional[datetime] = Field(None, description="Fecha vencimiento")
    ProximoVencer: bool = Field(..., description="Proximo vencer")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")
    Archivos: List[FileInfoModel] = Field(default_factory=list, description="Archivos")
    Ubicacion: str = Field(..., description="Ubicacion")
    Comentarios: str = Field(..., description="Comentarios")
    HallazgoComentarios: str = Field(..., description="Hallazgo comentarios")
    HallazgoRecomendaciones: str = Field(..., description="Hallazo requerimiento")