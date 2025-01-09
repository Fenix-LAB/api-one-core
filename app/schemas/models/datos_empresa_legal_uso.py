from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DatosEmpresaLegalUsoModel(BaseModel):
    PaisCode: str = Field(..., description="Pais code")
    EstadoCode: str = Field(..., description="Estado code")
    EstadoNombre: str = Field(..., description="Estado nombre")
    Municipio: str = Field(..., description="Municipio")
    Localidad: str = Field(..., description="Localidad")
    Colonia: str = Field(..., description="Colonia")
    Calle: str = Field(..., description="Calle")
    NumeroExterior: str = Field(..., description="Numero exterior")
    NumeroInterior: str = Field(..., description="Numero interior")
    CP: str = Field(..., description="CP")
    TipoDocumento: Optional[int] = Field(None, description="Tipo documento")
    FechaInicioVigencia: Optional[datetime] = Field(None, description="Fecha inicio vigencia")