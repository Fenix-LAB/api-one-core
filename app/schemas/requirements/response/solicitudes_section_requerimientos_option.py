from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class SolicitudesSectionRequerimientosOptionResponse(BaseModel):
    Code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    Cantidad: int = Field(..., description="Cantidad")
    Total: int = Field(..., description="Total")
    CantidadSolicitudes: int = Field(..., description="Cantidad solicitudes")