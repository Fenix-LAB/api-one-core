from pydantic import BaseModel, Field
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class SolicitudesSectionRequerimientosOptionResponse(BaseModel):
    code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    cantidad: int = Field(..., description="Cantidad")
    total: int = Field(..., description="Total")
    cantidadSolicitudes: int = Field(..., description="Cantidad solicitudes")