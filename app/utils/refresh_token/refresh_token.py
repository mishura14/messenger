import os
from datetime import UTC, datetime, timedelta

from dotenv import load_dotenv
from jose import jwt

load_dotenv()


# функция создания refresh_token
def create_refresh_token(user_id: int):
    expire = datetime.now(UTC) + timedelta(days=30)
    to_encode = {"sub": str(user_id), "type": "refresh", "exp": expire}

    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(
        to_encode, str(os.getenv("SECRET_KEY")), str(os.getenv("ALGORITHM"))
    )
