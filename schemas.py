from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str
    password: str
    
class UserLogin(BaseModel):
    user_id: str
    password: str   
    
class UserUpdate(BaseModel):
    new_user_id: str
    new_password: str   
    
class UserResponse(BaseModel):
    id: int
    user_id: str

    model_config = {
        "from_attributes": True
    }