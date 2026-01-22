from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import schemas
from services import admin_service

from typing import List


router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-user")
def create_user(
    admin_id: str,
    admin_password: str,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    admin_service.admin_auth(admin_id, admin_password)
    admin_service.create_user_service(db, user)
    return {"message": "User created successfully"}

@router.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(
    admin_id: str,
    admin_password: str,
    db: Session = Depends(get_db)
):
    admin_service.admin_auth(admin_id, admin_password)
    return admin_service.get_all_users_service(db)
