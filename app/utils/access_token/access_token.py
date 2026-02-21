import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import jwt

load_dotenv()


# функция создания access_token
def create_access_token(user_id: int):
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {"sub": str(user_id), "type": "access", "exp": expire}

    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(
        to_encode, str(os.getenv("SECRET_KEY")), str(os.getenv("ALGORITHM"))
    )
