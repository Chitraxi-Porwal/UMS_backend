from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, auth

def login_service(db: Session, user):
    db_user = db.query(models.User).filter(
        models.User.user_id == user.user_id
    ).first()

    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return db_user

def update_user_service(db: Session, user_id: str, password: str, update):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id
    ).first()

    if not db_user or not auth.verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    db_user.user_id = update.new_user_id
    db_user.password = auth.hash_password(update.new_password)

    db.commit()
    return db_user
