from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode
from uuid import UUID

class RequerimientosEvidenciaIDRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    codeSection: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")