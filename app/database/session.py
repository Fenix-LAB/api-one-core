from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from contextlib import asynccontextmanager
from config.config import config
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncIterator

from config.config import config

# Cadena de conexión a PostgreSQL
POSTGRES_STRING_CONNECTION = (
    f"postgresql+asyncpg://{config.ONE_CORE_DB_USER}:{config.ONE_CORE_DB_PASSWORD}"
    f"@{config.ONE_CORE_DB_HOST}:{config.ONE_CORE_DB_PORT}/{config.ONE_CORE_DB_NAME}"
)

# Crear motores de lectura y escritura
engine = create_async_engine(POSTGRES_STRING_CONNECTION, pool_recycle=3600)

# Crear una fábrica de sesiones
async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Base para modelos declarativos
class Base(DeclarativeBase):
    pass


# Proveer sesiones como dependencia de FastAPI
async def get_db_session() -> AsyncIterator[AsyncSession]:
    session = async_session_factory()
    try:
        yield session
    finally:
        await session.close()