from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class UserCreateModel(BaseModel):
    first_name: str = Field(max_length = 25)
    last_name: str = Field(max_length = 25)
    username: str = Field(max_length = 8)
    email: str = Field(max_length = 40)
    password: str = Field(max_length = 6)

class Usermodel(BaseModel):
    uid : uuid.UUID 
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime 
    update_at: datetime
    

class UserLoginModel(BaseModel):
    email: str = Field(max_length = 40)
    password: str = Field(max_length = 6)