from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class ClienteProveedorSaveRequest(BaseModel):
    id: UUID = Field(..., description="Id")
    status: int = Field(..., description="Status")
    isCompany: bool = Field(..., description="Is company")
    name: str = Field(..., description="Name")
    tipo: Optional[int] = Field(None, description="Tipo")  # Assuming DatosEmpresaClienteProveedorType is a string
    apellidoPaterno: str = Field(..., description="Apellido paterno")
    apellidoMaterno: str = Field(..., description="Apellido materno")
    tipoMovimiento: Optional[int] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaTipoMovimiento is a string
    fechaMovimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    aviso: str = Field(..., description="Aviso")
    paisCode: str = Field(..., description="Pais code")
    estadoCode: str = Field(..., description="Estado code")
    municipio: str = Field(..., description="Municipio")
    localidad: str = Field(..., description="Localidad")
    colonia: str = Field(..., description="Colonia")
    calle: str = Field(..., description="Calle")
    numeroExterior: str = Field(..., description="Numero exterior")
    numeroInterior: str = Field(..., description="Numero interior")
    cp: str = Field(..., description="Cp")
    telefono: str = Field(..., description="Telefono")