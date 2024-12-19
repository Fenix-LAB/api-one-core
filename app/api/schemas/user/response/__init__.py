from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
