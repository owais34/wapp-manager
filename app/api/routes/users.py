from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.api.deps import get_current_user
from app.utils import crud_user


router = APIRouter()


@router.post("/admin/add_user", response_model=UserOut)
def add_user(payload: UserCreate):
    existing = crud_user.get_user_by_username(payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user = crud_user.create_user(payload.username, payload.password, payload.is_admin)
    return user


@router.get("/me", response_model=UserOut)
def me(current_user = Depends(get_current_user)):
    return current_user