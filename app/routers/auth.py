from fastapi import APIRouter, Depends, HTTPException, Response, status

from app import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app import utils
from app.models import User

router = APIRouter(
    prefix="/login",
)


@router.post("/")
def create_user(user_credentials: schemas.UserCreate, db: Session = Depends(get_db)):
    user =    db.query(User).filter(User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=404, detail="invalid credentials")
    return user

    return {"message": "success"}
