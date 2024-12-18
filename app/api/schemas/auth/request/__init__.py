from pydantic import BaseModel, Field


class RefreshTokenRequest(BaseModel):
    Token: str = Field(..., description="Token")
    Refresh_token: str = Field(..., description="Refresh token")


class LoginTokenRequest(BaseModel):
    Token: str = Field(..., description="Token")
