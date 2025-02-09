from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class RequerimientoElementResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    verificacion: int = Field(..., description="Verificacion")  # Using lowercase 'v' for consistency
    usuario: Optional[str] = Field(..., description="Usuario")
    elementos: str = Field(..., description="Elementos")
    vencimiento: str = Field(..., description="Vencimiento")
    fechaEnvio: Optional[datetime] = Field(None, description="Fecha envio")
    esCritico: bool = Field(..., description="Es critico")