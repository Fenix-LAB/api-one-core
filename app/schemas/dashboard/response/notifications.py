from pydantic import BaseModel, Field
from datetime import datetime

class NotificationResponse(BaseModel):
    # id: int = Field(..., description="ID")
    titulo: str = Field(..., description="Titulo")
    referencia: str = Field(..., description="Referencia")
    estado: str = Field(..., description="Estado")
    descripcion: str = Field(..., description="Descripcion")
    fecha: datetime = Field(..., description="Fecha")
    esError: bool = Field(..., description="Es error")