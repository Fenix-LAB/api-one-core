# from app.database.models import Base
from app.database.models.models import Base
from config.logger_config import logger


async def create_tables(engine):
    logger.info("SQL: Creating tables ...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        logger.info("SQL: Tables created successfully!!!")
    await engine.dispose()
    logger.info("SQL: Engine disposed")
