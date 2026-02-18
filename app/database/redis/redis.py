import redis


def redis_connect():
    try:
        r = redis.Redis(host="localhost", port=6379, decode_responses=True)
        r.ping()
        print("Redis connected ✅")
        return r
    except redis.ConnectionError:
        print("Redis connection failed ❌")
        raise
