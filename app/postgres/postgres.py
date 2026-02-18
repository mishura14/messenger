import sys

import psycopg

db = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
}


def db_connect():
    try:
        conn = psycopg.connect(**db)
        if conn:
            print("Connected to PostgreSQL")
            return conn
    except Exception:
        sys.exit("Failed to connect to PostgreSQL")
