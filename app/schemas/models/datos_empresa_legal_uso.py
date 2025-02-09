from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DatosEmpresaLegalUsoModel(BaseModel):
    paisCode: str = Field(..., description="Pais code")
    estadoCode: str = Field(..., description="Estado code")
    estadoNombre: str = Field(..., description="Estado nombre")
    municipio: str = Field(..., description="Municipio")
    localidad: str = Field(..., description="Localidad")
    colonia: str = Field(..., description="Colonia")
    calle: str = Field(..., description="Calle")
    numeroExterior: str = Field(..., description="Numero exterior")
    numeroInterior: str = Field(..., description="Numero interior")
    cp: str = Field(..., description="CP")