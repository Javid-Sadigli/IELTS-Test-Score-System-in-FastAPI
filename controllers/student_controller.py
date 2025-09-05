from sqlalchemy.orm import Session
from models.student import Student

def get_all_students(db: Session):
    return db.query(Student).all()