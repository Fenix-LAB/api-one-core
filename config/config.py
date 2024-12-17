import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    JWT_SECRET_KEY: str = "your_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SENTRY_SDN: str = ""
    EXCLUDED_URLS: list[str] = ["/api/auth/login", "/docs", "/redoc", "/openapi.json"]


class TestConfig(Config):
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"


class LocalConfig(Config):
    APP_HOST: str = "127.0.0.1"
    JWT_SECRET_KEY: str = "43611869c1ed09fe5388ecbc8b3eab582f2c5c4fe22a2ed8de1fe9455c10267c"
    JWT_ALGORITHM: str = "HS256"


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
