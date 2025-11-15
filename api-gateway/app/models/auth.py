from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, ConfigDict


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

    _id: ObjectId
    username: str
    expiry: datetime