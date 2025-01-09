from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SocioAccionistaResponse(BaseModel):
    ID: int = Field(..., description="ID")
    CaseNumber: int = Field(..., description="Case number")
    IsCompany: bool = Field(..., description="Is company")
    Nombre: str = Field(..., description="Nombre")
    RFC: str = Field(..., description="RFC")
    CaracterCode: str = Field(..., description="Caracter code")
    CaracterDescripcion: str = Field(..., description="Caracter descripcion")
    IsObligadoTributar: bool = Field(..., description="Is obligado tributar")
    NombreEmpresa: str = Field(..., description="Nombre empresa")
    TipoMovimiento: Optional[str] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaSocioAccionistaTipoMovimiento is a string
    EscrituraPublica: int = Field(..., description="Escritura publica")
    FechaEscritura: Optional[datetime] = Field(None, description="Fecha escritura")