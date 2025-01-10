from pydantic import BaseModel, Field
from typing import List

class FileInfoModel(BaseModel):
    ID: int = Field(..., description="ID")
    Nombre: str = Field(..., description="Nombre")
    Extension: str = Field(..., description="Extension")
    Tamano: int = Field(..., description="Tamano")
    Contenido: List[int] = Field(..., description="Contenido")  # Representing byte array as list of integers
    FormatoTamano: str = Field(..., description="Formato tamano")
    Url: str = Field(..., description="Url")
    Selected: bool = Field(..., description="Selected")