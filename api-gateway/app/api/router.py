from fastapi import APIRouter

from app.api.routes import auth, admin, user

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
api_router.include_router(user.router, prefix="/user", tags=["User"])