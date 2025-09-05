from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from db.db import get_db
from controllers import student_controller

router = APIRouter()

@router.get("/")
def get_all_students(db: Session = Depends(get_db)):
    return student_controller.get_all_students(db)

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = student_controller.get_student_by_id(db, student_id)
    if not student:
        return {"error": "Student not found"}
    return student