from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.schemas import book
from app.db.session import get_db

router = APIRouter()

@router.post("/books/", response_model=book.Book)
def create_book(book_data: book.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book_data=book_data)

@router.get("/books/{book_id}", response_model=book.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.get("/books/popular/", response_model=list[book.Book])
def read_popular_books(db: Session = Depends(get_db)):
    return crud.get_popular_books(db=db)
