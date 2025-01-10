from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class HallazgoSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    CodeSection: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    EsHallazgo: bool = Field(..., description="Es hallazgo")
    Comentarios: str = Field(..., description="Comentarios")
    HallazgoCode: str = Field(..., description="Hallazgo code")
    HallazgoComentarios: str = Field(..., description="Hallazgo comentarios")
    Recomendaciones: str = Field(..., description="Recomendaciones")