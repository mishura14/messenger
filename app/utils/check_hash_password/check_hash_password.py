from passlib.context import CryptContext


# функция хеширования пароля
def hash_password(password: str, hash_password: str) -> bool:
    crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return crypt_context.verify(password, hash_password)
