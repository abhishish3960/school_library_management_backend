from pydantic import BaseModel

class InventoryBase(BaseModel):
    book_id: int
    student_id: int

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True
