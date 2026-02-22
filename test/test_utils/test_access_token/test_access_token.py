import os

from jose import jwt

from app.utils.access_token.access_token import create_access_token


# тест создания access_token
def test_create_access_token():
    token = create_access_token(1)
    assert token is not None


# тест типа данных токена
def test_access_token_type():
    token = create_access_token(1)
    assert isinstance(token, str)


# тест прверки снутриности токена
def test_access_token_structure():
    token = create_access_token(1)
    payload = jwt.decode(
        token,
        str(os.getenv("SECRET_KEY")),
        algorithms=[str(os.getenv("ALGORITHM"))],
    )

    assert payload["sub"] == str(1)
    assert payload["type"] == "access"
    assert "exp" in payload
