import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-local-trocar-em-producao")
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
    REDIS_DB = int(os.environ.get("REDIS_DB", "0"))
