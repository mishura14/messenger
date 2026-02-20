from fastapi import HTTPException

from app.core.core import rd
from app.model.model import CodeRegister
from app.Repository.user_repo import register_user
from app.Repository.user_repo_redis import get_verification_data


# хендлер для подтверждения регистрации
def confirm_register(code: CodeRegister):
    # Получаем данные пользователя из Redis
    user = get_verification_data(rd, code.code)
    if not user:
        raise HTTPException(
            status_code=400, detail="Неверный или просроченный код подтверждения"
        )

    # создаем пользователя в базе данных
    register_user(user["name"], user["email"], user["password"])
    # удаляем данные пользователя из Redis
    rd.delete(f"verify:{code.code}")
    return {"message": "регистрация подтверждена"}
