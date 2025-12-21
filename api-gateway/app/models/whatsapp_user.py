from typing import Optional, List
from bson import ObjectId
from app.models.common import IdModel
from pydantic import BaseModel


class WhatsappUser(IdModel):
    name: Optional[str] = None
    country_code: Optional[str] = None
    number: Optional[str] = None
    assigned_user_ids: Optional[List[ObjectId]] = None

class WhatsappUserCreate(BaseModel):
    name: Optional[str] = None
    country_code: Optional[str] = None
    number: Optional[str] = None

