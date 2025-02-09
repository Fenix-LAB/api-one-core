from pydantic import BaseModel, Field
from uuid import UUID

class HallazgoOptionModel(BaseModel):
    id: UUID = Field(..., description="Id")
    code: str = Field(..., description="Code")
    nombre: str = Field(..., description="Nombre")