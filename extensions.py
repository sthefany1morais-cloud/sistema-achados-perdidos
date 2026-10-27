import redis
from flask import current_app

class RedisExtension:
    def init_app(self, app):
        app.extensions["redis_client"] = redis.Redis(
            host=app.config["REDIS_HOST"],
            port=app.config["REDIS_PORT"],
            db=app.config["REDIS_DB"],
            decode_responses=True,
            socket_connect_timeout=3,
            health_check_interval=30,
        )

redis_client = RedisExtension()

def get_redis():
    return current_app.extensions["redis_client"]
