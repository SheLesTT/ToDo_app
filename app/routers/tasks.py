from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Task
from ..import schemas

router = APIRouter(
    prefix="/tasks",
)

posts = [{"id":"1","name":"aa", "content": "Hello World"},{"id":"2","name":"bb", "content": "Hello World"}]
@router.get("/")
async def get_posts():
    return posts[0]

@router.get("/{id}", response_model=schemas.Task)
async def get_post(id:int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="User not found")

    return task
