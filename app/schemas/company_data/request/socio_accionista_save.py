from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class SocioAccionistaSaveRequest(BaseModel):
    id: UUID = Field(..., description="ID")
    status: int = Field(..., description="Registro status")  # Assuming RegistroStatus is a string
    isCompany: bool = Field(..., description="Is company")
    nombre: str = Field(..., description="Nombre")
    rfc: str = Field(..., description="RFC")
    caracterCode: str = Field(..., description="Caracter code")
    isObligadoTributar: bool = Field(..., description="Is obligado tributar")
    nombreEmpresa: str = Field(..., description="Nombre empresa")
    tipoMovimiento: Optional[int] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaSocioAccionistaTipoMovimiento is a string
    escrituraPublica: Optional[str] = Field(None, description="Escritura publica")
    fechaEscritura: Optional[datetime] = Field(None, description="Fecha escritura")
    fedatario: str = Field(..., description="Fedatario")
    numeroNotario: Optional[str] = Field(None, description="Numero notario")
    efectoEscrituraPublica: int = Field(..., description="Efecto escritura publica")
    aviso: str = Field(..., description="Aviso")
    fechaAviso: Optional[datetime] = Field(None, description="Fecha aviso")