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