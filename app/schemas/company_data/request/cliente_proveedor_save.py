from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ClienteProveedorSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    IsCompany: bool = Field(..., description="Is company")
    Name: str = Field(..., description="Name")
    Tipo: Optional[str] = Field(None, description="Tipo")  # Assuming DatosEmpresaClienteProveedorType is a string
    ApellidoPaterno: str = Field(..., description="Apellido paterno")
    ApellidoMaterno: str = Field(..., description="Apellido materno")
    TipoMovimiento: Optional[str] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaTipoMovimiento is a string
    FechaMovimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    Aviso: str = Field(..., description="Aviso")
    PaisCode: str = Field(..., description="Pais code")
    EstadoCode: str = Field(..., description="Estado code")
    Municipio: str = Field(..., description="Municipio")