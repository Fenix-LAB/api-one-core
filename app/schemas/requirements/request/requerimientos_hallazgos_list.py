from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class RequerimientosHallazgosListRequest(BaseModel):
    codeSection: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")