from fastapi import HTTPException, status, Request

from app.core.security import decode_access_token
from app.utils import user


async def get_current_user(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.lower().startswith("bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header"
        )
    token = auth_header.split(" ")[1].strip()
    try:
        token_payload = decode_access_token(token)
        user = crud_user.get_user_by_id(token_payload.id)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired JWT"
        )


async def get_current_admin_user(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.lower().startswith("bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header"
        )
    token = auth_header.split(" ")[1].strip()
    try:
        token_payload = decode_access_token(token)
        user = crud_user.get_user_by_id(token_payload.id)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        if not user.get("is_admin"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not admin")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired JWT"
        )