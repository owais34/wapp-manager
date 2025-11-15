from typing import Optional

from pymongo import MongoClient
from pymongo.synchronous.database import Database

from app.core.config import SETTINGS

MONGO_CLIENT: Optional[MongoClient]= None
DATABASE: Optional[Database] = None

def get_database_client():
    global MONGO_CLIENT
    if MONGO_CLIENT is None:
        MONGO_CLIENT = MongoClient(SETTINGS.MONGO_URI)
    return MONGO_CLIENT

# Dependency for FastAPI routes
def get_database():
    global DATABASE
    if DATABASE is None:
        client = get_database_client()
        DATABASE = client[SETTINGS.MONGO_DB]
    return DATABASE