from fastapi import APIRouter,Depends
from bson import ObjectId
from app.utils.functions import get_current_user, get_current_admin_user


class AuthenticatedAPIRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dependencies.append(Depends(get_current_user))


class AdminAPIRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dependencies.append(Depends(get_current_admin_user))


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate


    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)
