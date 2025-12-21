from fastapi import APIRouter, HTTPException
from datetime import timedelta

from app.models.auth import LoginRequest
from app.utils.user import get_user_by_username
from app.core.security import verify_password, create_access_token
from app.utils.constants import ADMIN_ROLE

router = APIRouter()

@router.post("/login")
def login(payload: LoginRequest):
    user = get_user_by_username(payload.username)
    if not user or not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user, expires_delta=timedelta(minutes=60))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/admin/login")
def login(payload: LoginRequest):
    user = get_user_by_username(payload.username)
    if not user or not verify_password(payload.password, user["hashed_password"]) or not user["role"] == ADMIN_ROLE:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user, expires_delta=timedelta(minutes=60))
    return {"access_token": access_token, "token_type": "bearer"}
