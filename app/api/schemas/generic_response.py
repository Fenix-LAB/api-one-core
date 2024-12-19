from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    Status: str
    Message: Optional[str]
    Data: Optional[T]
    Token: Optional[str]


class ApiResponseNoToken(BaseModel, Generic[T]):
    Status: str
    Message: Optional[str]
    Data: Optional[T]
