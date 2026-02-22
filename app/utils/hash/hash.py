import hashlib

from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str) -> str:
    sha = hashlib.sha256(password.encode()).hexdigest()
    return crypt_context.hash(sha)
