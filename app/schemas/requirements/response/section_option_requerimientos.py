from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class SectionOptionRequerimientosResponse(BaseModel):
    Code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    Cantidad: int = Field(..., description="Cantidad")
    Total: int = Field(..., description="Total")
    ProximosVencer: int = Field(..., description="Proximos vencer")
    Selected: bool = Field(..., description="Selected")
    Enable: bool = Field(..., description="Enable")