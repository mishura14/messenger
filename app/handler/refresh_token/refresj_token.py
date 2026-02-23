from fastapi.exceptions import HTTPException

from app.model.model import RefreshUpdate
from app.repository.user_repo import get_refresh_token, update_refresh_token
from app.utils.access_token.access_token import create_access_token
from app.utils.check_hash.check_hash import check_hash
from app.utils.decoder_refresh_token.decoder_refresh_token import decoder_refresh_token
from app.utils.hash.hash import hash
from app.utils.refresh_token.refresh_token import create_refresh_token


# обновление refresh token
def refresh_update_token(refresh_token: RefreshUpdate):
    payload = decoder_refresh_token(refresh_token.refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    refresh_hash = get_refresh_token(int(payload))
    if not refresh_hash:
        raise HTTPException(status_code=401, detail="Invalid refresh token db")

    if not check_hash(refresh_token.refresh_token, refresh_hash["hash_refresh_token"]):
        raise HTTPException(status_code=401, detail="Invalid time refresh token ")

    access_token = create_access_token(int(payload))
    new_refresh_token = create_refresh_token(int(payload))

    update_refresh_token(int(payload), hash(new_refresh_token))
    return {"access_token": access_token, "refresh_token": new_refresh_token}
