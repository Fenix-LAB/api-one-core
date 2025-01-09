from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProveedorNacionalSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    RFC: str = Field(..., description="RFC")
    ValorOperaciones: Optional[float] = Field(None, description="Valor operaciones")
    Porcentaje: Optional[float] = Field(None, description="Porcentaje")
    IsOpinionPositiva: bool = Field(..., description="Is opinion positiva")
    IsOperacionesVirtuales: bool = Field(..., description="Is operaciones virtuales")
    FechaMovimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    Aviso: str = Field(..., description="Aviso")
    FechaAviso: Optional[datetime] = Field(None, description="Fecha aviso")