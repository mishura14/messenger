import os

from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

load_dotenv()


# функция декодирования токена обновления
def decoder_refresh_token(token: str):
    try:
        payload = jwt.decode(
            token,
            str(os.getenv("SECRET_KEY")),
            algorithms=[str(os.getenv("ALGORITHM"))],
        )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный тип токена",
            )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Токен не содержит идентификатор пользователя",
            )

        return str(user_id)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh токен истек",
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный refresh токен",
        )
