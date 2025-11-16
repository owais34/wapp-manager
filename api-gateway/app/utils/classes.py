from fastapi import APIRouter,Depends

from app.utils.functions import get_current_user, get_current_admin_user


class AuthenticatedAPIRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dependencies.append(Depends(get_current_user))


class AdminAPIRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dependencies.append(Depends(get_current_admin_user))

