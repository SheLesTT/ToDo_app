from pydantic import BaseModel, EmailStr
from typing import Optional


class Task(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    is_done: bool

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    content: Optional[str] = None

    class Config:
        from_attirbutes = True


class TaskUpdateContent(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_done: Optional[bool] = None

    class Config:
        from_attirbutes = True


class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

    class Config:
        from_attirbutes = True


class UserCreate(UserBase):
    email: EmailStr
    password: str
class UserLogin():
    email: EmailStr
    password: str
class User(UserBase):
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None