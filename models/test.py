from sqlalchemy import Column, Integer, ForeignKey, Double
from sqlalchemy.orm import relationship
from typing import ClassVar
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
    
    total_score : ClassVar[Double]
    
    @property
    def calculate_total_score(self):
        total_score_not_rounded = (self.reading_score + self.writing_score + self.listening_score + self.speaking_score) / 4
        self.total_score = ielts_round(total_score_not_rounded)
        
        
def ielts_round(score):
    decimal = score - int(score)
    if decimal < 0.25:
        return int(score)
    elif decimal < 0.75:
        return int(score) + 0.5
    else:
        return int(score) + 1