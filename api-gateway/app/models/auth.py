from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class TokenPayload(BaseModel):
    user_id: str
    expiry: datetime
    auth_level: str

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        extra="ignore",
        json_encoders={
            datetime: lambda v: v.isoformat(),
        },
    )

    @field_validator("expiry", mode="before")
    def convert_date(cls, value):
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except:
                raise ValueError("Invalid Date string")
        return value


class LoginRequest(BaseModel):
    username: str
    password: str
