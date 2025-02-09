from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_enlace_operativo import DatosEmpresaEnlaceOperativoModel
from uuid import UUID
from datetime import datetime

class EnlaceOperativoSaveRequest(BaseModel):
    id: UUID = Field(..., description="Id")
    status: int = Field(..., description="Status")
    nombre: str = Field(..., description="Nombre")
    paisCode: str = Field(..., description="Pais Code")
    estadoCode: str = Field(..., description="Estado Code")
    estadoNombre: str = Field(..., description="Estado Nombre")
    puesto: str = Field(..., description="Puesto")
    email: str = Field(..., description="Email")
    telefono: str = Field(..., description="Telefono")
    tipoMovimiento: int = Field(..., description="Tipo Movimiento")
    fechaMovimiento: datetime = Field(..., description="Fecha Movimiento")
    aviso: str = Field(..., description="Aviso")
    fechaAviso: datetime = Field(..., description="Fecha Aviso")