from pydantic import BaseModel, Field
from datetime import datetime

class NotificationResponse(BaseModel):
    ID: int = Field(..., description="ID")
    Titulo: str = Field(..., description="Titulo")
    Referencia: str = Field(..., description="Referencia")
    Estado: str = Field(..., description="Estado")
    Descripcion: str = Field(..., description="Descripcion")
    Fecha: datetime = Field(..., description="Fecha")
    EsError: bool = Field(..., description="Es error")