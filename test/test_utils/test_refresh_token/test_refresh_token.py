import os

from jose import jwt

from app.utils.refresh_token.refresh_token import create_refresh_token


# тест создания refresh_token
def test_create_refresh_token():
    token = create_refresh_token(1)
    assert token is not None


# тест типа данных токена
def test_token_type():
    token = create_refresh_token(1)
    assert isinstance(token, str)


# тест прверки снутриности токена
def test_token_structure():
    token = create_refresh_token(1)
    payload = jwt.decode(
        token,
        str(os.getenv("SECRET_KEY")),
        algorithms=[str(os.getenv("ALGORITHM"))],
    )

    assert payload["sub"] == str(1)
    assert payload["type"] == "refresh"
    assert "exp" in payload
