from pydantic import BaseModel, Field

class DatosEmpresaSocioAccionistaCaracterModel(BaseModel):
    code: str = Field(..., description="Code")
    description: str = Field(..., description="Description")