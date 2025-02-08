from pydantic import BaseModel, Field


class LoginResponse(BaseModel):
    token: str = Field(..., description="Token")
