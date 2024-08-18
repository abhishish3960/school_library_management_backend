from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    borrowed_books_count: int

    class Config:
        orm_mode = True
