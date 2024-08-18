from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    total_copies: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    issued_copies: int

    class Config:
        orm_mode = True
