from pydantic import BaseModel
from typing import Generic, List, TypeVar

T = TypeVar("T")


class ListResponse(BaseModel, Generic[T]):
    CurrentPage: int
    PageSize: int
    TotalPages: int
    TotalRecords: int
    Data: List[T]
