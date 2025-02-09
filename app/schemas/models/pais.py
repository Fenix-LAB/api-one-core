from pydantic import BaseModel, Field
from uuid import UUID

class PaisModel(BaseModel):
    id: UUID = Field(..., description="Id")
    paisCode: str = Field(..., description="Pais code")
    telefonoCode: str = Field(..., description="Telefono code")