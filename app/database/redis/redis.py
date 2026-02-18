import os

import redis
from dotenv import load_dotenv

load_dotenv()


def redis_connect():
    try:
        r = redis.Redis(
            host=str(os.getenv("REDIS_HOST")),
            port=6379,
            decode_responses=True,
        )
        r.ping()
        print("Redis connected ✅")
        return r
    except redis.ConnectionError:
        print("Redis connection failed ❌")
        raise
