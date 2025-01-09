from pydantic import BaseModel, Field

class HallazgoOptionModel(BaseModel):
    ID: int = Field(..., description="ID")
    Code: str = Field(..., description="Code")
    Nombre: str = Field(..., description="Nombre")