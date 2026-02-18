import os
import smtplib


def create_smtp_server():
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(str(os.getenv("EMAIL_USER")), str(os.getenv("EMAIL_PASSWORD")))
    return server
