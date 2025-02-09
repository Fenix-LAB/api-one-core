from pydantic import BaseModel, Field
from app.schemas.models.area_rol import AreaRolType

class ResponsableModel(BaseModel):
    id: int = Field(..., description="ID")
    nombre: str = Field(..., description="Nombre")
    areaCode: AreaRolType = Field(..., description="Area code")