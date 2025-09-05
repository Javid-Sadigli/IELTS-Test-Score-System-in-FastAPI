from sqlalchemy import Column, Integer, ForeignKey, Double
from sqlalchemy.orm import relationship
from db.db import Base

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True, index=True)
    reading_score = Column(Double, nullable=False)
    writing_score = Column(Double, nullable=False)
    listening_score = Column(Double, nullable=False)
    speaking_score = Column(Double, nullable=False)
    
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    
    student = relationship("Student", back_populates="tests")