from pydantic import BaseModel, Field
from typing import List
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.file_info import FileInfoModel

class RequerimientosEvidenciaSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")
    Archivos: List[FileInfoModel] = Field(default_factory=list, description="Archivos")
    Ubicacion: str = Field(..., description="Ubicacion")
    Comentarios: str = Field(..., description="Comentarios")