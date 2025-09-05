from fastapi import FastAPI
from db import Base, engine
from models import User

# Run migrations
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}