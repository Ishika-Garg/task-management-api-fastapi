from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models, crud, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@app.get("/")
def home():

    return {
        "message": "Task Management API Running"
    }

@app.post("/tasks/")
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):

    return crud.create_task(db=db, task=task)

@app.get("/tasks/")
def read_tasks(
    db: Session = Depends(get_db)
):

    return crud.get_tasks(db)