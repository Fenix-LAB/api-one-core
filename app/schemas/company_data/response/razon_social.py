from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RazonSocialResponse(BaseModel):
    ID: int = Field(..., description="ID")
    CaseNumber: int = Field(..., description="Case number")
    IsCompany: bool = Field(..., description="Is company")
    Name: str = Field(..., description="Name")
    RFC: str = Field(..., description="RFC")
    Folio: str = Field(..., description="Folio")
    MovementDate: Optional[datetime] = Field(None, description="Movement date")
    DeedDate: Optional[datetime] = Field(None, description="Deed date")
    Fedatario: str = Field(..., description="Fedatario")
    Notary: str = Field(..., description="Notary")
    Effect: Optional[str] = Field(None, description="Effect")  # Assuming DatosEmpresaTypeEscrituraPublica is a string
    Notice: str = Field(..., description="Notice")
    NoticeDate: Optional[datetime] = Field(None, description="Notice date")