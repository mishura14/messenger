from fastapi import FastAPI

from app.database.postgres.postgres import db_connect
from app.database.redis.redis import redis_connect
from app.handler.register_handler import register_handler
from app.utils.smtp.smtp_register import send_verification_email
from app.utils.smtp.smtp_server import create_smtp_server

# Подключение к postgres
db_connect()
# Подключение к redis
redis_connect()
# инициализация почтового сервера
server = create_smtp_server()
# Подключение к postgres
db_connect()
# запуск сервера
app = FastAPI()
# добавление роутера для регистрации
app.include_router(register_handler.register_router)
