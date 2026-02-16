from psycopg.rows import dict_row

from app.database.postgres.postgres import db_connect
from app.model.model import UserRegister


# функция провeрки пользователя по email
def check_user_by_email(email):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cur.fetchone()


# функция регистрации пользователя
def register_user(user: UserRegister):
    with db_connect() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (user.name, user.email, user.password),
            )
            conn.commit()
            return cur.fetchone()
