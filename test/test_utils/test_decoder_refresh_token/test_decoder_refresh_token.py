import time

from app.utils.decoder_refresh_token.decoder_refresh_token import decoder_refresh_token
from app.utils.refresh_token.refresh_token import create_refresh_token


# тест декодирования токена доступа с неверным токеном
def test_decode_refres_token():
    user_id = 1
    token = create_refresh_token(user_id)
    decode_token = decoder_refresh_token(token)
    assert int(decode_token) == user_id
