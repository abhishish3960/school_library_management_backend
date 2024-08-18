from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.schemas import student
from app.db.session import get_db

router = APIRouter()

@router.post("/students/", response_model=student.Student)
def create_student(student_data: student.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student_data=student_data)

@router.get("/students/{student_id}", response_model=student.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
