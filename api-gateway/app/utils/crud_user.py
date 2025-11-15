from typing import Optional, Dict, Any

from bson import ObjectId

from app.db.constants import USERS
from app.db.session import get_database
from app.models.user import UserModel
from app.core.security import hash_password

db = get_database()

def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    return db[USERS].find_one({"username": username})

def get_user_by_id(user_id: str) -> Optional[Dict[str, Any]]:
    return db[USERS].find_one({"_id": ObjectId(user_id)})


def create_user(username: str, password: str, is_admin: bool = False):
    user = UserModel(username=username, hashed_password=hash_password(password), is_admin=is_admin)
    if not db[USERS].find_one({"username": username}):
        db[USERS].insert_one(user.model_dump(by_alias=True))
    return user