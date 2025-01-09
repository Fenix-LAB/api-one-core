from pydantic import BaseModel, Field

class DatosEmpresaSocioAccionistaCaracterModel(BaseModel):
    Code: str = Field(..., description="Code")
    Description: str = Field(..., description="Description")