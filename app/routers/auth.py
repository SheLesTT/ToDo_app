from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from app import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from app import utils, oauth2
from app.models import User

router = APIRouter(
    prefix="/login",
)


@router.post("/")
def create_user(user_credentials: OAuth2PasswordRequestForm, db: Session = Depends(get_db)):
    user =    db.query(User).filter(User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=404, detail="invalid credentials")

    access_toke = oauth2.create_access_token({"user_id": user.id})
    return {"access_token": access_toke, "token_type": "bearer"}
