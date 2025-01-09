from pydantic import BaseModel, Field

class EnlaceOperativoResponse(BaseModel):
    ID: int = Field(..., description="ID")
    CaseNumber: int = Field(..., description="Case number")
    Nombre: str = Field(..., description="Nombre")
    RFC: str = Field(..., description="RFC")
    TipoRelacion: str = Field(..., description="Tipo relacion")
    FechaInicio: str = Field(..., description="Fecha inicio")
    FechaFin: str = Field(..., description="Fecha fin")
    Observaciones: str = Field(..., description="Observaciones")