from fastapi import APIRouter

from app.handler.confirm_register_handler.confirm_register_hendler import (
    confirm_register,
)
from app.handler.register_handler.register_handler import RegisterHandler

auth_router = APIRouter()

auth_router.post("/confirm")(confirm_register)
auth_router.post("/register")(RegisterHandler)
