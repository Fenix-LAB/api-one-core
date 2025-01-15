from pydantic import BaseModel, Field


class RequerimientoObligacionesResponse(BaseModel):
    Pendientes: int = Field(..., description="Number of pending requirements")
    Proximos: int = Field(..., description="Number of requirements near due date")
    Hallazgos: int = Field(..., description="Number of findings")