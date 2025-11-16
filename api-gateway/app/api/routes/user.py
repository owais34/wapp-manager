from app.schemas.user import UserOut
from app.utils.classes import AuthenticatedAPIRouter

router = AuthenticatedAPIRouter()


@router.get("", response_model=UserOut)
def get_user():

    return user
