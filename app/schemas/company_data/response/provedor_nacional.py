from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class ProveedorNacionalResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    rfc: str = Field(..., description="RFC")
    valorOperaciones: Optional[float] = Field(None, description="Valor operaciones")
    porcentaje: Optional[float] = Field(None, description="Porcentaje")
    isOpinionPositiva: bool = Field(..., description="Is opinion positiva")
    isOperacionesVirtuales: bool = Field(..., description="Is operaciones virtuales")
    fechaMovimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    aviso: str = Field(..., description="Aviso")
    fechaAviso: Optional[datetime] = Field(None, description="Fecha aviso")