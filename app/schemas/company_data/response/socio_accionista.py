from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class SocioAccionistaResponse(BaseModel):
    id: UUID = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    isCompany: bool = Field(..., description="Is company")
    nombre: str = Field(..., description="Nombre")
    rfc: str = Field(..., description="RFC")
    caracterCode: str = Field(..., description="Caracter code")
    caracterDescripcion: str = Field(..., description="Caracter descripcion")
    isObligadoTributar: bool = Field(..., description="Is obligado tributar")
    nombreEmpresa: str = Field(..., description="Nombre empresa")
    tipoMovimiento: Optional[str] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaSocioAccionistaTipoMovimiento is a string
    escrituraPublica: int = Field(..., description="Escritura publica")
    fechaEscritura: Optional[datetime] = Field(None, description="Fecha escritura")
    fedatario: str = Field(..., description="Fedatario")
    numeroNotario: str = Field(..., description="Numero notario")
    efectoEscrituraPublica: str = Field(..., description="Efecto escritura publica")
    aviso: str = Field(..., description="Aviso")
    fechaAviso: Optional[datetime] = Field(None, description="Fecha aviso")