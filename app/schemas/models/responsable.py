from pydantic import BaseModel, Field
from app.schemas.models.area_rol import AreaRolType

class ResponsableModel(BaseModel):
    ID: int = Field(..., description="ID")
    Nombre: str = Field(..., description="Nombre")
    AreaCode: AreaRolType = Field(..., description="Area code")