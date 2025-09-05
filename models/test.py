from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True, index=True)
    reading_score = Column(Integer, nullable=False)
    writing_score = Column(Integer, nullable=False)
    listening_score = Column(Integer, nullable=False)
    speaking_score = Column(Integer, nullable=False)
    student = relationship("Student", back_populates="tests")