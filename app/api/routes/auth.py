from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta
from app.schemas.user import LoginRequest, Token
from app.db.session import get_database
from app.utils import crud_user
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db = Depends(get_database)):
    user = crud_user.get_user_by_username(payload.username)
    if not user or not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user, expires_delta=timedelta(minutes=60))
    return {"access_token": access_token, "token_type": "bearer"}