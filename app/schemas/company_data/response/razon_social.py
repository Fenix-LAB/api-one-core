from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RazonSocialResponse(BaseModel):
    id: int = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    isCompany: bool = Field(..., description="Is company")
    name: str = Field(..., description="Name")
    rfc: str = Field(..., description="RFC")
    folio: str = Field(..., description="Folio")
    movementDate: Optional[datetime] = Field(None, description="Movement date")
    deedDate: Optional[datetime] = Field(None, description="Deed date")
    fedatario: str = Field(..., description="Fedatario")
    notary: str = Field(..., description="Notary")
    effect: Optional[str] = Field(None, description="Effect")  # Assuming DatosEmpresaTypeEscrituraPublica is a string
    notice: str = Field(..., description="Notice")
    noticeDate: Optional[datetime] = Field(None, description="Notice date")