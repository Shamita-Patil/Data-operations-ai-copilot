import redis

from backend.app.core.config import settings


redis_client = redis.Redis(
    host="redis",
    port=6379,
    db=0,
    decode_responses=True,
)


def get_redis():

    return redis_client