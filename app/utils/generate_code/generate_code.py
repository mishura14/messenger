import random


# функция для генерации кода подтверждения
def generate_verification_code() -> str:
    return f"{random.randint(100000, 999999)}"
