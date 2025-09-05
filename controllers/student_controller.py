from sqlalchemy.orm import Session
from models.student import Student

def get_all_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, full_name: str, email: str):
    new_student = Student(full_name=full_name, email=email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student