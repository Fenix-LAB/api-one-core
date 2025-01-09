from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DatosEmpresaEnlaceOperativoModel(BaseModel):
    Nombre: str = Field(..., description="Nombre")
    PaisCode: str = Field(..., description="Pais code")
    EstadoCode: str = Field(..., description="Estado code")
    EstadoNombre: str = Field(..., description="Estado nombre")
    Puesto: str = Field(..., description="Puesto")
    Email: str = Field(..., description="Email")
    Telefono: str = Field(..., description="Telefono")
    TipoMovimiento: Optional[str] = Field(None, description="Tipo movimiento")  # Assuming DatosEmpresaTipoMovimiento is a string
    FechaMovimiento: Optional[datetime] = Field(None, description="Fecha movimiento")
    Aviso: str = Field(..., description="Aviso")
    FechaAviso: Optional[datetime] = Field(None, description="Fecha aviso")