import os
from email.message import EmailMessage


# функция отправки кода подтверждения на почту
def send_verification_email(server, to_email: str, code: str):
    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email
    msg["Subject"] = "Код подтверждения регистрации"

    msg.set_content(
        f"""
Ваш код подтверждения: {code}

Код действителен 5 минут.
Если вы не регистрировались — просто проигнорируйте письмо.
"""
    )

    server.send_message(msg)
