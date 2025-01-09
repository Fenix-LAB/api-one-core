from pydantic import BaseModel, Field
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode

class DatosEmpresaHallazgosListRequest(BaseModel):
    CodeSection: IvaSectionOptionCode = Field(..., description="Iva Section Option Code")