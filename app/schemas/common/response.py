from pydantic import BaseModel, Field


class ResponsableResponse(BaseModel):
    ID: int = Field(..., description="ID")
    Nombre: str = Field(..., description="Name")
    AreaCode: str = Field(..., description="Area code")
