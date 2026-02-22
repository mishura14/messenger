from app.model.model import UserLogin
from app.repository.user_repo import get_user_by_email, insert_refresh_token
from app.utils.access_token.access_token import create_access_token
from app.utils.check_hash.check_hash import check_hash
from app.utils.hash.hash import hash
from app.utils.refresh_token.refresh_token import create_refresh_token


# функция входа в аккаунт
def LoginHandler(user: UserLogin):
    # получение данныъ пользователя по email
    user_db = get_user_by_email(user.email)
    if not user_db:
        return {"error": "User not found"}
    # проверка хэша пароля
    if not check_hash(user.password, user_db["password"]):
        return {"error": "Invalid password"}
    # создание токенов
    refresh = create_refresh_token(user_db["id"])
    if not refresh:
        return {"error": "Failed to create refresh token"}
    access = create_access_token(user_db["id"])
    if not access:
        return {"error": "Failed to create access token"}

    refreshHash = hash(refresh)
    insert_refresh_token(user_db["id"], refreshHash)

    return {"refresh": refresh, "access": access}
