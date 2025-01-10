from pydantic import BaseModel, Field

class TotalSolicitudesRevisorResponse(BaseModel):
    Solicitudes: int = Field(..., description="Solicitudes")