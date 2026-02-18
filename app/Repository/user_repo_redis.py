# функция сохранения кода подтверждения в Redis
def save_code_redis(redis_client, email: str, code: str):
    redis_client.setex(f"verify:{email}", 300, code)
