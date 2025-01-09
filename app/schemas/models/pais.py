from pydantic import BaseModel, Field

class PaisModel(BaseModel):
    PaisCode: str = Field(..., description="Pais code")
    TelefonoCode: str = Field(..., description="Telefono code")