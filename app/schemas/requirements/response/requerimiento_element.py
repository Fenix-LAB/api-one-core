from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RequerimientoElementResponse(BaseModel):
    ID: int = Field(..., description="ID")
    Verificacion: str = Field(..., description="Verificacion")  # Assuming RegistroStatus is a string
    Usuario: str = Field(..., description="Usuario")
    Elementos: str = Field(..., description="Elementos")
    Vencimiento: str = Field(..., description="Vencimiento")
    FechaEnvio: Optional[datetime] = Field(None, description="Fecha envio")
    EsCritico: bool = Field(..., description="Es critico")