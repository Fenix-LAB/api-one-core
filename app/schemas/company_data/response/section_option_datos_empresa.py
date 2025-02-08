from pydantic import BaseModel, Field
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode

class SectionOptionDatosEmpresaResponse(BaseModel):
    code: IvaSectionOptionCode = Field(..., description="Enum code, see IvaSectionOptionCode [RazonSocial, Domicilio, ClienteExtranjero, ProveedorNacional, SociosAccionistas, LegalUso, EnlacesOperativos]")
    cantidad: int = Field(..., description="Cantidad")
    total: int = Field(..., description="Total")
    selected: bool = Field(..., description="Selected")
