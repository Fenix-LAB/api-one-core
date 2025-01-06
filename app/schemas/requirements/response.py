from pydantic import BaseModel, Field


class RequerementsObligationsResponse(BaseModel):
    Pending: int = Field(..., description="Pendientes")
    NearDue: int = Field(..., description="Proximos")
    Findings: int = Field(..., description="Hallazgos")