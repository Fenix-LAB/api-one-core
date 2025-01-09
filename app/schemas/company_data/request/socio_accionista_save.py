from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SocioAccionistaSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    IsCompany: bool = Field(..., description="Is company")
    Nombre: str = Field(..., description="Nombre")
    RFC: str = Field(..., description="RFC")
    CaracterCode: str = Field(..., description="Caracter code")
    IsObligadoTributar: bool = Field(..., description="Is obligado tributar")
    NombreEmpresa: str = Field(..., description="Nombre empresa")
    TipoMovimiento: Optional[str] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaSocioAccionistaTipoMovimiento is a string
    EscrituraPublica: Optional[int] = Field(None, description="Escritura publica")
    FechaEscritura: Optional[datetime] = Field(None, description="Fecha escritura")
    Fedatario: str = Field(..., description="Fedatario")
    NumeroNotario: Optional[int] = Field(None, description="Numero notario")