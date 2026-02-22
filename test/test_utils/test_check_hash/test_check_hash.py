from app.utils.check_hash import check_hash
from app.utils.hash.hash import hash


# проверка на правильность пароля
def test_check_hash_password():
    password = "mishura"
    hash_password = hash(password)
    assert check_hash.check_hash(password, hash_password)


# тест на неправильность пароля
def test_check_hash_password_wrong_password():
    password = "mishura"
    hash_password = hash(password)
    assert not check_hash.check_hash("wrong_password", hash_password)


#
