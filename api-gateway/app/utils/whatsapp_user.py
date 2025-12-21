from typing import Dict, Any

from app.db.constants import WHATSAPP_USERS
from app.db.session import get_database
from bson import ObjectId

db = get_database()

def count_unauthenticated_users() -> int:
    return db[WHATSAPP_USERS].count_documents({"authenticated": False})


def get_whatsapp_user(country_code: str, number: str) -> Dict[str, Any]:
    return db[WHATSAPP_USERS].find_one({"country_code": country_code, "number": number})


def create_new_whatsapp_user(name: str, country_code: str, number: str) -> ObjectId:
    result = db[WHATSAPP_USERS].insert_one({"authenticated": False, "name": name, "country_code": country_code,
                                            "number": number})
    return result.inserted_id


def spawn_whatsapp_session(account_id: ObjectId):
    # TODO: Implement logic
    pass