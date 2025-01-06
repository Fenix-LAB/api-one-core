from pydantic import BaseModel, Field


class LoginResponse(BaseModel):
    Token: str = Field(..., description="Token")
