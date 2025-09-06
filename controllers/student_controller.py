from sqlalchemy.orm import Session
from models.student import Student
from . import test_controller

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

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return True
    return False

def update_student(db: Session, student_id: int, full_name: str = None, email: str = None):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None
    if full_name is not None:
        student.full_name = full_name
    if email is not None:
        student.email = email
    db.commit()
    db.refresh(student)
    return student

def get_student_tests(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)
    if not student:
        return {"error": "Student not found"}
    return test_controller.get_tests_by_student_id(db, student_id)