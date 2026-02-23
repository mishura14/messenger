from fastapi import APIRouter

from app.handler.confirm_register_handler.confirm_register_hendler import (
    confirm_register,
)
from app.handler.login_handler.login_handler import LoginHandler
from app.handler.refresh_token.refresj_token import refresh_update_token
from app.handler.register_handler.register_handler import RegisterHandler

auth_router = APIRouter()

auth_router.post("/confirm")(confirm_register)
auth_router.post("/register")(RegisterHandler)
auth_router.post("/login")(LoginHandler)
auth_router.post("/refresh_token")(refresh_update_token)
