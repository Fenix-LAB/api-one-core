from pydantic import BaseModel, Field
from enum import Enum


class AreaRolType(Enum):
    Administrador = "Administrador"
    Rrhh = "Rrhh"
    Finanzas = "Finanzas"
    Fiscal = "Fiscal"
    Comex = "Comex"
    Legal = "Legal"
    Revisor = "Revisor"


class AreaRolModel(BaseModel):
    Code: AreaRolType = Field(..., description="Area rol type code")
    Name: str = Field(..., description="Name")


