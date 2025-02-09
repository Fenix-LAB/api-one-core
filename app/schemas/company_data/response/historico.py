from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Generic, TypeVar, List

T = TypeVar('T')

class HistoricoResponse(BaseModel, Generic[T]):
    status: str = Field(..., description="Registro status")  # Assuming RegistroStatus is a string
    usuario: str = Field(..., description="Usuario")
    fecha: Optional[datetime] = Field(None, description="Fecha")
    data: T = Field(..., description="Data")
    # data: List[T] = [] # Assuming Data is a list of T