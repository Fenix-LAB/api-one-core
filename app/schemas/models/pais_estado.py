from pydantic import BaseModel, Field

class PaisEstadoModel(BaseModel):
    PaisCode: str = Field(..., description="Pais code")
    EstadoCode: str = Field(..., description="Estado code")
    EstadoName: str = Field(..., description="Estado name")