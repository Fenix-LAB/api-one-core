from pydantic import BaseModel, Field

class EstadosRequest(BaseModel):
    PaisCode: str = Field(..., description="Pais code")