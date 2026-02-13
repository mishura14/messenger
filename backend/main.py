from app.handler.register_handler.register_handler import (
    router as register_router,
)
from app.postgres.postgres import db_connect
from fastapi import FastAPI

# Подключение к postgres
db_connect()

app = FastAPI()
# добавление роутера для регистрации
app.include_router(register_router)
