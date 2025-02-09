from pydantic import BaseModel, Field
from uuid import UUID

class EstadosRequest(BaseModel):
    idPais: UUID = Field(..., description="Id Pais")