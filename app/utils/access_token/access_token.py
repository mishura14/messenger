import os
from datetime import UTC, datetime, timedelta

from dotenv import load_dotenv
from jose import jwt

load_dotenv()


def create_access_token(user_id: int):
    expire = datetime.now(UTC) + timedelta(minutes=15)

    payload = {
        "sub": str(user_id),
        "type": "access",
        "exp": expire,
    }

    return jwt.encode(
        payload,
        str(os.getenv("SECRET_KEY")),
        str(os.getenv("ALGORITHM")),
    )
