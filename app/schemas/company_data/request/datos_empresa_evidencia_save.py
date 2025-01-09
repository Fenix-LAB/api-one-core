from pydantic import BaseModel, Field
from typing import List
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode
from app.schemas.models import AreaRolModel
from app.schemas.models import ResponsableModel
from app.schemas.models.hallazgo_option_model import HallazgoOptionModel

class DatosEmpresaEvidenciaSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    CodeSection: IvaSectionOptionCode = Field(..., description="Iva Section Option Code")
    IsHallazgo: bool = Field(..., description="Is hallazgo")
    AreaRols: List[AreaRolModel] = Field(..., description="Area roles")
    Responsables: List[ResponsableModel] = Field(..., description="Responsables")
    Recomendaciones: str = Field(..., description="Recomendaciones")
    Hallazgo: HallazgoOptionModel = Field(..., description="Hallazgo")
    HallazgoComentarios: str = Field(..., description="Hallazgo comentarios")