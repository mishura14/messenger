from fastapi import Header, HTTPException

from app.utils.decoder_access_token import decoder_access_token
from app.utils.decoder_access_token.decoder_access_token import decode_access_token


def user_middleware(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        sheme, token = authorization.split()

        if sheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authorization scheme")

        payload = decoder_access_token.decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
