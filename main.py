from fastapi import FastAPI

from app.router.auth_router import auth_router

# запуск сервера
app = FastAPI()
# добавление роутера для регистрации
app.include_router(auth_router, prefix="/auth")
