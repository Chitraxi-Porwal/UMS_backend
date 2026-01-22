from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import schemas
from services import user_service

router = APIRouter(tags=["User"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user_service.login_service(db, user)
    return {"message": "Login successful"}

@router.put("/user/update")
def update_user(
    user_id: str,
    password: str,
    update: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    user_service.update_user_service(db, user_id, password, update)
    return {"message": "User credentials updated"}
