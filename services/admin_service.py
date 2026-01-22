from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, auth

ADMIN_ID = "admin"
ADMIN_PASSWORD = "1234"

def admin_auth(admin_id: str, admin_password: str):
    if admin_id != ADMIN_ID or admin_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid Admin")

def create_user_service(db: Session, user):
    existing_user = db.query(models.User).filter(
        models.User.user_id == user.user_id
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User ID already registered")

    new_user = models.User(
        user_id=user.user_id,
        password=auth.hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all_users_service(db: Session):
    return db.query(models.User).all()
