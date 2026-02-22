from app.core.core import rd, server
from app.model.model import UserRegister
from app.Repository.user_repo import check_user_by_email
from app.Repository.user_repo_redis import save_code_redis
from app.utils.generate_code.generate_code import generate_verification_code
from app.utils.hash import hash
from app.utils.smtp.smtp_register import send_verification_email


# хендлер регистрации
def RegisterHandler(user: UserRegister):
    # проверка на существование пользователя
    if check_user_by_email(user.email):
        return {"error": "user already exists"}
    # хеширование пароля
    passwordHash = hash.hash(user.password)
    # генерация кода
    code = generate_verification_code()
    # отправка кода на почту
    send_verification_email(server, user.email, code)
    # сохранение кода в redis
    save_code_redis(rd, user.name, user.email, passwordHash, code)

    return {
        "message": "код регистрации отправлен на вашу почту он действителен в течении 5 минут"
    }
