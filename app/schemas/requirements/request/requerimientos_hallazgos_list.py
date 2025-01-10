from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class RequerimientosHallazgosListRequest(BaseModel):
    CodeSection: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")