from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: int
    name: str
    content: Optional[str] =None
    is_done: bool

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    name: str
    content: Optional[str] = None

    class Config:
        orm_mode = True
class TaskUpdateContent(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None
    is_done: Optional[bool] = None

    class Config:
        orm_mode = True
