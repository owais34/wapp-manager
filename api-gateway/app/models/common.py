from typing import Optional
from bson import ObjectId
from app.utils.classes import PyObjectId
from pydantic import BaseModel, Field


class IdModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True