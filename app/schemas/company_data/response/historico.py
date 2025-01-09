from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class HistoricoResponse(BaseModel, Generic[T]):
    Status: str = Field(..., description="Registro status")  # Assuming RegistroStatus is a string
    Usuario: str = Field(..., description="Usuario")
    Fecha: Optional[datetime] = Field(None, description="Fecha")
    Data: T = Field(..., description="Data")