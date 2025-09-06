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

@router.post("/")
def create_student(full_name: str = Body(...), email: str = Body(...), db: Session = Depends(get_db)):
    return student_controller.create_student(db, full_name, email)

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    success = student_controller.delete_student(db, student_id)
    if not success:
        return {"error": "Student not found or could not be deleted"}
    return {"message": "Student deleted successfully"}

@router.put("/{student_id}")
def update_student(
    student_id: int, 
    full_name: str = Body(None), 
    email: str = Body(None), 
    db: Session = Depends(get_db)
):
    student = student_controller.update_student(db, student_id, full_name, email)
    if not student:
        return {"error": "Student not found or could not be updated"}
    return student

@router.get("/{student_id}/tests")
def get_student_tests(student_id: int, db: Session = Depends(get_db)):
    student_tests = student_controller.get_student_tests(db, student_id)
    if student_tests is None:
        return {"error": "Student not found"}
    return student_tests