from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.schemas import inventory
from app.db.session import get_db

router = APIRouter()

@router.post("/inventory/issue/", response_model=inventory.Inventory)
def issue_book(inventory_data: inventory.InventoryCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db=db, student_id=inventory_data.student_id)
    if db_student.borrowed_books_count >= 3:
        raise HTTPException(status_code=400, detail="Student has reached the limit of 3 books")

    db_book = crud.get_book_by_id(db=db, book_id=inventory_data.book_id)
    if db_book.issued_copies >= db_book.total_copies:
        raise HTTPException(status_code=400, detail="Book is not available in inventory")

    crud.update_book_inventory(db=db, book_id=inventory_data.book_id, issued=True)
    crud.update_student_books_count(db=db, student_id=inventory_data.student_id, borrowed=True)
    
    return crud.issue_book(db=db, inventory_data=inventory_data)

@router.delete("/inventory/return/{inventory_id}", response_model=inventory.Inventory)
def return_book(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.return_book(db=db, inventory_id=inventory_id)
    crud.update_book_inventory(db=db, book_id=db_inventory.book_id, issued=False)
    crud.update_student_books_count(db=db, student_id=db_inventory.student_id, borrowed=False)
    return db_inventory
