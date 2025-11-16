from fastapi import HTTPException
from app.schemas.user import UserCreate, UserOut
from app.utils import crud_user
from app.utils.classes import AdminAPIRouter

router = AdminAPIRouter()


@router.post("/add_user", response_model=UserOut)
def add_user(payload: UserCreate):
    existing = crud_user.get_user_by_username(payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user = crud_user.create_user(payload.username, payload.password, payload.is_admin)
    return user
