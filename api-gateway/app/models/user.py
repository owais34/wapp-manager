from typing import Optional
from app.models.common import IdModel


class User(IdModel):
    username: Optional[str] = None
    is_admin: Optional[bool] = None


class UserCreate(User):
    password: Optional[str] = None

