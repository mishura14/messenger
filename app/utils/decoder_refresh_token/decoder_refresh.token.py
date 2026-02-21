import os

from dotenv import load_dotenv
from fastapi import HTTPException
from jose import jwt

load_dotenv()


# функция декодирования токена обновления
def decode_refresh_token(token: str):
    payload = jwt.decode(
        token, str(os.getenv("SECRET_KEY")), algorithms=[str(os.getenv("ALGORITHM"))]
    )

    if payload.get("type") == "refresh":
        raise HTTPException(status_code=400, detail="Invalid token type")

    return payload.get("sub")
