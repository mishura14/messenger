from fastapi import Depends

from app.middleware.login_middleware.login_middleware import user_middleware
from app.repository.user_repo import delete_refresh_token


def logout(user_id: int = Depends(user_middleware)):
    delete_refresh_token(user_id)
    return {"message": "Logged out successfully"}
