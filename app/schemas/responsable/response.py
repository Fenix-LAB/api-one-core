from pydantic import BaseModel, Field


class ResponsableResponse(BaseModel):
    id: int = Field(..., description="ID")
    name: str = Field(..., description="Name")
    area_code: str = Field(..., description="Area code")
