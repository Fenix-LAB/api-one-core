from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    email: str = Field(..., description="Email")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
