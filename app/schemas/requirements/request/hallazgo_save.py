from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode
from uuid import UUID

class HallazgoSaveRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    codeSection: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    esHallazgo: bool = Field(..., description="Es hallazgo")
    comentarios: str = Field(..., description="Comentarios")
    hallazgoID: UUID = Field(..., description="Hallazgo ID")
    hallazgoComentarios: str = Field(..., description="Hallazgo comentarios")
    recomendaciones: str = Field(..., description="Recomendaciones")