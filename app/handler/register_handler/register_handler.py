from fastapi import APIRouter

from app.model.model import UserRegister

register_router = APIRouter(prefix="/auth")


@register_router.post("/register")
def RegisterHandler(user: UserRegister):

    return {"message": "User registered successfully"}
