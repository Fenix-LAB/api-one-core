from pydantic import BaseModel, Field
from typing import List
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode
from app.schemas.models import AreaRolModel
from app.schemas.models import ResponsableModel
from app.schemas.models import HallazgoOptionModel
from uuid import UUID

class DatosEmpresaEvidenciaSaveRequest(BaseModel):
    id: UUID = Field(..., description="Id")
    status: int = Field(..., description="Status")
    codeSection: IvaSectionOptionCode = Field(..., description="Iva Section Option Code")
    idHallazgo: UUID = Field(..., description="Id Hallazgo")
    areaRols: List[AreaRolModel] = Field(..., description="Area roles")
    responsables: List[ResponsableModel] = Field(..., description="Responsables")
    recomendaciones: str = Field(..., description="Recomendaciones")
    # hallazgo: HallazgoOptionModel = Field(..., description="Hallazgo")
    hallazgoComentarios: str = Field(..., description="Hallazgo comentarios")