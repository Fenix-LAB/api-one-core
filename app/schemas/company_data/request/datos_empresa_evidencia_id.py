from pydantic import BaseModel, Field
from app.schemas.enums.iva_section_option_code import IvaSectionOptionCode
from uuid import UUID

class DatosempresaEvidenciaIDRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    codeSection: IvaSectionOptionCode = Field(..., description="Iva Section Option Code")