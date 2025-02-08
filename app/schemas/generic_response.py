from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: Optional[str]
    data: Optional[T]
    token: Optional[str]


class ApiResponseNoToken(BaseModel, Generic[T]):
    success: bool
    message: Optional[str]
    data: Optional[T]
