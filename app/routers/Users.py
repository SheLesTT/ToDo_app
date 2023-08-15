from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from .. import schemas
from app.utils import hash_password
router = APIRouter(
    prefix="/users",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, name=user.name, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @app.get("/users", response_model=list[schemas.User])
