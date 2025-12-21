from fastapi import HTTPException

from app.models.whatsapp_user import WhatsappUserCreate
from app.models.user import UserCreate, User
from app.utils.user import get_user_by_username, create_user
from app.utils.classes import AdminAPIRouter
from app.utils.whatsapp_user import get_whatsapp_user, count_unauthenticated_users, create_new_whatsapp_user, \
    spawn_whatsapp_session

router = AdminAPIRouter()


@router.post("/add_user", response_model=User)
def add_user(payload: UserCreate):
    existing = get_user_by_username(payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user = create_user(payload.username, payload.password, payload.is_admin)
    return user


@router.post("/add_whatsapp_account")
def add_whatapp_user(payload: WhatsappUserCreate):
    count_un_auth_users = count_unauthenticated_users()
    if count_un_auth_users > 2:
        raise HTTPException(status_code=400, detail=f"{count_un_auth_users} un-authenticated accounts already exist.")
    existing = get_whatsapp_user(payload.country_code, payload.number)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user_id = create_new_whatsapp_user(payload.name, payload.country_code, payload.number)
    spawn_whatsapp_session(user_id)