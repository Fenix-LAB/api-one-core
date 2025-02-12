from pydantic import BaseModel
from typing import Generic, List, TypeVar

T = TypeVar("T")


class ListResponse(BaseModel, Generic[T]):
    currentPage: int
    pageSize: int
    totalPages: int
    totalRecords: int
    data: List[T] = []
