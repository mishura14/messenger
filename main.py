from app.handler.register_handler import register_handler
from app.postgres.postgres import db_connect
from fastapi import FastAPI

# Подключение к postgres
db_connect()
# запуск сервера
app = FastAPI()
# добавление роутера для регистрации
app.include_router(register_handler.register_router)
