from passlib.context import CryptContext


# функция хеширования пароля
def hash_password(password: str) -> str:
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return crypt_context.hash(password)
