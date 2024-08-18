from sqlalchemy.orm import Session
from app.db import models
from app.schemas import book, student, inventory

# Book-related operations
def create_book(db: Session, book_data: book.BookCreate):
    db_book = models.Book(**book_data.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book_inventory(db: Session, book_id: int, issued: bool):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if issued:
        db_book.issued_copies += 1
    else:
        db_book.issued_copies -= 1
    db.commit()
    return db_book

# Student-related operations
def create_student(db: Session, student_data: student.StudentCreate):
    db_student = models.Student(**student_data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def update_student_books_count(db: Session, student_id: int, borrowed: bool):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if borrowed:
        db_student.borrowed_books_count += 1
    else:
        db_student.borrowed_books_count -= 1
    db.commit()
    return db_student

# Inventory-related operations
def issue_book(db: Session, inventory_data: inventory.InventoryCreate):
    db_inventory = models.Inventory(**inventory_data.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def return_book(db: Session, inventory_id: int):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    db.delete(db_inventory)
    db.commit()
    return db_inventory

# Popular books
def get_popular_books(db: Session, limit: int = 5):
    return db.query(models.Book).order_by(models.Book.issued_copies.desc()).limit(limit).all()
