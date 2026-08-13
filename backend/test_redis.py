from backend.app.cache.redis import redis_client
import time

redis_client.set(
    "language",
    "Python",
    ex=10,
)

print(redis_client.get("language"))

time.sleep(11)

print("After 11 seconds:", redis_client.get("language"))