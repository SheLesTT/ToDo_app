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
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("here username", user_credentials.username, user_credentials.password)
    user =   db.query(User).filter(User.email == user_credentials.username).first()
    print("maby after")

    if not user:
        print("this is mistake")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        print("not this", user_credentials.password,"thecond password", user.password)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    print("or in the end")
    access_token = oauth2.create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
