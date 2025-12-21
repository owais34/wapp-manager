from typing import List

from app.db.constants import USERS
from app.db.session import get_database
from app.models.user import User
from app.utils.classes import AuthenticatedAPIRouter

router = AuthenticatedAPIRouter()

db = get_database()

@router.get("", response_model=List[User])
def get_user():
    return list(db[USERS].find({"is_admin": False}))
