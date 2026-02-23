from fastapi import APIRouter

from app.handler.logout_handler.logout_handler import logout

user_router = APIRouter()


user_router.post("/logout")(logout)
