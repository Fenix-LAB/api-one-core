from pydantic import BaseModel, Field
from typing import List
from uuid import UUID

class FileInfoModel(BaseModel):
    id: UUID = Field(..., description="ID")
    nombre: str = Field(..., description="Nombre")
    extension: str = Field(..., description="Extension")
    tamano: int = Field(..., description="Tamano")
    contenido: str = Field(..., description="Contenido")  # Representing byte array as list of integers
    formatoTamano: str = Field(..., description="Formato tamano")
    url: str = Field(..., description="Url")
    ubicacion: str = Field(..., description="Ubicacion")
    selected: bool = Field(..., description="Selected")