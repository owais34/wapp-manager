from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

from app.utils.classes import PyObjectId


class MongoModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True


class UserModel(MongoModel):
    username: Optional[str] = None
    hashed_password: Optional[str] = None
    is_admin: Optional[bool] = None
