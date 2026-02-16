from fastapi import FastAPI

from app.database.postgres.postgres import db_connect
from app.handler.register_handler import register_handler

# Подключение к postgres
db_connect()
# запуск сервера
app = FastAPI()
# добавление роутера для регистрации
app.include_router(register_handler.register_router)
