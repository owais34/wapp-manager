from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from starlette import status

from app.core.config import SETTINGS
from app.core.logging_config import logger
from app.models.auth import TokenPayload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a plaintext password using bcrypt.
    Returns a salted hash suitable for storage in MongoDB.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify user-entered password against hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plain password for storage."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"expiry": expire})
    payload = TokenPayload.model_validate(to_encode).model_dump(mode="json")
    logger.debug(f"Payload: {payload}")
    return jwt.encode(payload, SETTINGS.SECRET_KEY, algorithm=SETTINGS.ALGORITHM)


def decode_access_token(token: str) -> dict:
    """
    Decode a JWT access token and return its payload.
    Raises an HTTPException if token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SETTINGS.SECRET_KEY, algorithms=[SETTINGS.ALGORITHM])
        username = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: subject missing",
            )
        return payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )