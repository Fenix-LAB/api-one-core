import os
import json

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080
    JWT_SECRET_KEY: str = "your_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    EXCLUDED_URLS: list[str] = ["/api/auth/login", "/docs", "/redoc", "/openapi.json"]
    ROUTE_PATH: str = "app/v1/"


class ProductionConfig(Config):
    with open("config.json") as f:
        production_conf = json.load(f)

    DEBUG: bool = production_conf["prod"]["debug"]
    APP_HOST: str = production_conf["prod"]["app"]["host"]
    APP_PORT: int = production_conf["prod"]["app"]["port"]
    JWT_SECRET: str = production_conf["prod"]["jwt"]["secret_key"]
    JWT_ALGORITHM: str = production_conf["prod"]["jwt"]["algorithm"]
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = production_conf["prod"]["jwt"]["access_token_expire_minutes"]
    WRITER_DB_URL: str = production_conf["prod"]["db"]["writer"]
    READER_DB_URL: str = production_conf["prod"]["db"]["reader"]
    EXCLUDED_URLS: list[str] = production_conf["prod"]["excluded_urls"]
    ROUTE_PATH: str = production_conf["prod"]["route_path"]


class TestConfig(ProductionConfig):
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"


class LocalConfig(Config):
    APP_HOST: str = "127.0.0.1"
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
