import time

from app.utils.access_token import access_token
from app.utils.decoder_access_token.decoder_access_token import decode_access_token


# тест декодирования токена доступа
def test_decode_access_token():
    user_id = 123412121234124
    token = access_token.create_access_token(user_id)
    decode_token = decode_access_token(token)
    assert int(decode_token) == user_id
