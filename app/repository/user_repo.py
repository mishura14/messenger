from datetime import datetime, timedelta

from psycopg.rows import dict_row

from app.database.postgres.postgres import db_connect


# функция провeрки пользователя по email
def check_user_by_email(email):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cur.fetchone()


# функция регистрации пользователя
def register_user(name: str, email: str, password: str):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (name, email, password),
            )
            conn.commit()
            return cur.fetchone()


# функция получающая данные пользователя по email
def get_user_by_email(email: str):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cur.fetchone()


# фукнция вставки данных refresh token
def insert_refresh_token(user_id: int, hash_refresh_token: str):
    expires = datetime.utcnow() + timedelta(days=30)
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                INSERT INTO refresh_tokens (user_id, hash_refresh_token, expires_at, created_at, revoked)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (user_id, hash_refresh_token, expires, datetime.utcnow(), False),
            )
            conn.commit()


# функция удаление refresh token
def delete_refresh_token(user_id: int):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                DELETE FROM refresh_tokens WHERE user_id = %s
                """,
                (user_id,),
            )
            conn.commit()
