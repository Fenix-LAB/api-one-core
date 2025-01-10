from pydantic import BaseModel, Field


class RequerimientoObligacionesResponse(BaseModel):
    Pending: int = Field(..., description="Number of pending requirements")
    NearDue: int = Field(..., description="Number of requirements near due date")
    Findings: int = Field(..., description="Number of findings")