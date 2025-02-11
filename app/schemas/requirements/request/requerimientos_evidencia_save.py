from pydantic import BaseModel, Field
from typing import List
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.file_info import FileInfoModel
from uuid import UUID

class RequerimientosEvidenciaSaveRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    areaRols: List[AreaRolModel] = Field(..., description="Area roles")
    responsables: List[ResponsableModel] = Field(..., description="Responsables")
    archivos: List[FileInfoModel] = Field(default_factory=list, description="Archivos")
    ubicacion: str = Field(..., description="Ubicacion")
    comentarios: str = Field(..., description="Comentarios")
    status: int = Field(..., description="Status")