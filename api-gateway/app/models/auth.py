from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, field_validator


class TokenPayload(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        extra="ignore",
        json_encoders={
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        },
    )

    @field_validator("_id", mode="before")
    def convert_object_id(cls, value):
        if isinstance(value, str):
            try:
                return ObjectId(value)
            except:
                raise ValueError("Invalid ObjectId string")
        return value

    @field_validator("expiry", mode="before")
    def convert_date(cls, value):
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except:
                raise ValueError("Invalid Date string")
        return value

    _id: ObjectId
    username: str
    expiry: datetime

    @property
    def id(self):
        return self._id