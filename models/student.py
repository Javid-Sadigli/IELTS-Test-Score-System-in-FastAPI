from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name= Column(String(50), nullable=False)
    email= Column(String(50), unique=True, index=True, nullable=False)
    tests = relationship("Test", back_populates="student")