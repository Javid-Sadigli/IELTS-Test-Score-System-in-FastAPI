from fastapi import FastAPI
from db.db import Base, engine
from routers import student_router, test_router


# Run migrations
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router.router, prefix="/students", tags=["students"])
app.include_router(test_router.router, prefix="/tests", tags=["tests"])