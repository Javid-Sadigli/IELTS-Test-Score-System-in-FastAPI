from sqlalchemy.orm import Session
from models.test import Test    
from . import student_controller

def create_test(db: Session, student_id: int, listening: float, reading: float, writing: float, speaking: float):
    student = student_controller.get_student_by_id(db, student_id)
    if not student:
        return {"error": "Student not found"}
    
    new_test = Test(
        student_id=student_id, 
        listening_score=listening, 
        reading_score=reading, 
        writing_score=writing, 
        speaking_score=speaking
    )
    
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test


def get_test_by_id(db: Session, test_id: int):
    test = db.query(Test).filter(Test.id == test_id).first()
    test.calculate_total_score()
    return test

def get_all_tests(db: Session):
    tests = db.query(Test).all()
    for test in tests:
        test.calculate_total_score()
    return tests

def delete_test(db: Session, test_id: int):
    test = db.query(Test).filter(Test.id == test_id).first()
    if test:
        db.delete(test)
        db.commit()
        return True
    return False

def get_tests_by_student_id(db: Session, student_id: int):
    tests = db.query(Test).filter(Test.student_id == student_id).all()
    for test in tests:
        test.calculate_total_score()
    return tests