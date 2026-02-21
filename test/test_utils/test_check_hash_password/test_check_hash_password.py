from app.utils.check_hash_password import check_hash_password
from app.utils.hash_password.hash_password import hash_password


# проверка на правильность пароля
def test_check_hash_password():
    password = "mishura"
    hash = hash_password(password)
    assert check_hash_password.verify_password(password, hash)


# тест на неправильность пароля
def test_check_hash_password_wrong_password():
    password = "mishura"
    hash = hash_password(password)
    assert not check_hash_password.verify_password("wrong_password", hash)


#
