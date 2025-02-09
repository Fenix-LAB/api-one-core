from pydantic import BaseModel, Field
from enum import Enum


class AreaRolType(Enum):
    Administrador = 0
    Rrhh = 1
    Finanzas = 2
    Fiscal = 3
    Comex = 4
    Legal = 5
    Revisor = 6


class AreaRolModel(BaseModel):
    code: AreaRolType = Field(..., description="Area rol type code")
    name: str = Field(..., description="Name")
