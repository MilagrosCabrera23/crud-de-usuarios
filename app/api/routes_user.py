from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user, get_users, delete_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No encontrado")
    return user

@router.delete("/users/{user_id}", response_model=UserResponse)
def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No encontrado")
    return user