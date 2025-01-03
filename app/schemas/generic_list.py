from pydantic import BaseModel
from typing import Generic, List, TypeVar

T = TypeVar("T")

class ListResponse(BaseModel, Generic[T]):
    current_page: int
    page_size: int
    total_pages: int
    total_records: int
    data: List[T]