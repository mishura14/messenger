import hashlib

from app.utils.hash import hash


# тест на то что хеш является строкой
def test_return_string():
    hash_password = hash.hash("123456")
    assert isinstance(hash_password, str)
    assert hash_password != "123456"


# тест на то что хеш не равен паролю
def test_hash_not_equal_password():
    password = "123456"
    hash_password = hash.hash(password)
    assert hash_password != password


# тест проверку генерации хеша
def test_can_verify_password():
    password = "123456"
    hash_password = hash.hash(password)

    sha = hashlib.sha256(password.encode()).hexdigest()

    assert hash.crypt_context.verify(sha, hash_password)


# тест на проверку пароля
def test_wrong_password():
    password = "123456"
    wrong_password = "1234567"
    hashed = hash.hash(password)
    wrong_hash = hash.hash(wrong_password)

    assert not hash.crypt_context.verify(wrong_hash, hashed)


# тест на то что хеш начинается с $2b$
def test_user_password():
    hashed = hash.hash("123456")
    assert hashed.startswith("$2b$")
