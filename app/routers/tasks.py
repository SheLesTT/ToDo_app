from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Task
from ..import schemas

router = APIRouter(
    prefix="/tasks",
)

posts = [{"id":"1","name":"aa", "content": "Hello World"},{"id":"2","name":"bb", "content": "Hello World"}]
@router.get("/", response_model=list[schemas.Task])
async def get_posts(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.get("/{id}", response_model=schemas.Task)
async def get_post(id:int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="User not found")
    return task


@router.post("/", response_model=schemas.Task)
async def create_post(post: schemas.TaskCreate, db: Session = Depends(get_db)):

    new_task = Task(name=post.name, content=post.content)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{id}")
async def update_content(id:int, task_update :schemas.TaskUpdateContent, db:Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task_update.content:
        task.content = task_update.content
    if task_update.name is not None:
        task.name = task_update.name
    if task_update.is_done is not None:
        task.is_done = task_update.is_done

    db.commit()
    db.refresh(task)
    return task


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db:Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
