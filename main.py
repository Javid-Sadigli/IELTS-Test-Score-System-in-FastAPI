from fastapi import FastAPI
from db.db import Base, engine
from routers import student_router
from models import student, test


# Run migrations
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router.router, prefix="/students", tags=["students"])