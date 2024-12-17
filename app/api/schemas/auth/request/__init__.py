from pydantic import BaseModel, Field


class RefreshTokenRequest(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")


class LoginTokenRequest(BaseModel):
    token: str = Field(..., description="Token")
