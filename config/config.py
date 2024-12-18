import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = os.getenv("APP_PORT", 8000)
    WRITER_DB_URL: str = os.getenv("WRITER_DB_URL", "None")
    READER_DB_URL: str = os.getenv("READER_DB_URL", "None")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "None")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    EXCLUDED_URLS: list[str] = os.getenv("EXCLUDED_URLS", ["/api/auth/login", "/docs", "/redoc", "/openapi.json"])
    ROUTE_PATH: str = os.getenv("ROUTE_PATH", "app/v1/routes")


class TestConfig(Config):
    WRITER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"
    READER_DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi_test"


class LocalConfig(Config):
    APP_HOST: str = "127.0.0.1"
    

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
