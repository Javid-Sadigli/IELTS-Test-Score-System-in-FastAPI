from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from db.db import get_db
from controllers import test_controller

router = APIRouter()

@router.post("/")
def create_test(
    student_id: int = Body(...), 
    listening: float = Body(...), 
    reading: float = Body(...), 
    writing: float = Body(...), 
    speaking: float = Body(...), 
    db: Session = Depends(get_db)
):
    return test_controller.create_test(db, student_id, listening, reading, writing, speaking)

@router.get("/{test_id}")
def get_test(test_id: int, db: Session = Depends(get_db)):
    test = test_controller.get_test_by_id(db, test_id)
    if not test:
        return {"error": "Test not found"}
    return test

@router.get("/")
def get_all_tests(db: Session = Depends(get_db)):
    return test_controller.get_all_tests(db)