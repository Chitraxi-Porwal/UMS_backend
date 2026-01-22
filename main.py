from fastapi import FastAPI
from database import engine, Base
from routers import admin, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router)
app.include_router(user.router)



