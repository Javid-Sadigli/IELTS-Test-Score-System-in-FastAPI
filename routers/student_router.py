from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from db.db import get_db
from controllers import student_controller

router = APIRouter()

@router.get("/")
def get_all_students(db: Session = Depends(get_db)):
    return student_controller.get_all_students(db)