from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class ProveedorNacionalResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    case_number: int = Field(..., description="Case number")
    rfc: str = Field(..., description="RFC")
    valor_operaciones: Optional[float] = Field(None, description="Valor operaciones")
    porcentaje: Optional[float] = Field(None, description="Porcentaje")
    is_opinion_positiva: bool = Field(..., description="Is opinion positiva")
    is_operaciones_virtuales: bool = Field(..., description="Is operaciones virtuales")
    fecha_movimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    aviso: str = Field(..., description="Aviso")
    fecha_aviso: Optional[datetime] = Field(None, description="Fecha aviso")