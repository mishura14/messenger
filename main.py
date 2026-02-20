from fastapi import FastAPI

from app.database.postgres.postgres import db_connect
from app.database.redis.redis import redis_connect
from app.handler.confirm_register_handler.confirm_register_hendler import (
    confirm_register,
)
from app.handler.register_handler import register_handler
from app.router.auth_router import auth_router
from app.utils.smtp.smtp_register import send_verification_email
from app.utils.smtp.smtp_server import create_smtp_server

# запуск сервера
app = FastAPI()
# добавление роутера для регистрации
app.include_router(auth_router, prefix="/auth")
