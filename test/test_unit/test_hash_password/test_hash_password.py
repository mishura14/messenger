import hashlib

from app.utils.hash_password import hash_password


# тест на то что хеш является строкой
def test_return_string():
    hash = hash_password.hash_password("123456")
    assert isinstance(hash, str)
    assert hash != "123456"


# тест на то что хеш не равен паролю
def test_hash_not_equal_password():
    password = "123456"
    hash = hash_password.hash_password(password)
    assert hash != password


# тест проверку генерации хеша
def test_can_verify_password():
    password = "123456"
    hash = hash_password.hash_password(password)

    sha = hashlib.sha256(password.encode()).hexdigest()

    assert hash_password.crypt_context.verify(sha, hash)


# тест на проверку пароля
def test_wrong_password():
    password = "123456"
    wrong_password = "1234567"
    hashed = hash_password.hash_password(password)
    wrong_hash = hash_password.hash_password(wrong_password)

    assert not hash_password.crypt_context.verify(wrong_hash, hashed)


# тест на то что хеш начинается с $2b$
def test_user_password():
    hashed = hash_password.hash_password("123456")
    assert hashed.startswith("$2b$")
