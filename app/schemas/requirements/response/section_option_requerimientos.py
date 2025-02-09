from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class SectionOptionRequerimientosResponse(BaseModel):
    code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    cantidad: int = Field(..., description="Cantidad")
    total: int = Field(..., description="Total")
    proximosVencer: int = Field(..., description="Proximos vencer")
    selected: bool = Field(..., description="Selected")
    enable: bool = Field(..., description="Enable")