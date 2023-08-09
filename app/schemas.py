from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    content: str
    is_done: bool

    class Config:
        orm_mode = True