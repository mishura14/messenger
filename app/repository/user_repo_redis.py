import json


# функция сохранения кода подтверждения в Redis
def save_code_redis(redis_client, name: str, email: str, password: str, code: str):
    data = {"name": name, "email": email, "password": password, "code": code}

    redis_client.setex(
        f"verify:{code}",
        300,  # 5 минут
        json.dumps(data),
    )


# функция получения данных для подтверждения из Redis
def get_verification_data(redis_client, code: str):
    data = redis_client.get(f"verify:{code}")

    if not data:
        return None

    return json.loads(data)
