from app.model.model import UserRegister
from fastapi import APIRouter

register_router = APIRouter(prefix="/auth")


@register_router.post("/register")
def RegisterHandler(user: UserRegister):

    return {"message": "User registered successfully"}
