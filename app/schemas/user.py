from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    name: str
    telefono: str
    fecha_nacimiento: date    
    email: EmailStr

class UserCreate(UserBase):
    password: str                 

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True