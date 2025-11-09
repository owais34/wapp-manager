from typing import Optional
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserBase(BaseModel):
    username: str
    is_admin: bool = False


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Plain text password for new user")


class UserOut(UserBase):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        from_attributes = True
        validate_by_name = True

