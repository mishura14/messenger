import psycopg

db = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
}


def db_connect():
    return psycopg.connect(**db)
