from pydantic import BaseModel, Field
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode

class SectionOptionDatosEmpresaResponse(BaseModel):
    Code: IvaSectionOptionCode = Field(..., description="Enum code, see IvaSectionOptionCode [RazonSocial, Domicilio, ClienteExtranjero, ProveedorNacional, SociosAccionistas, LegalUso, EnlacesOperativos]")
    Cantidad: int = Field(..., description="Cantidad")
    Total: int = Field(..., description="Total")
    Selected: bool = Field(..., description="Selected")
