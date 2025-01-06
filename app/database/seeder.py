from app.database.models import Base
from config.logger_config import logger
from app.database.models import Role

role_data = [
    {"name": "Administrador", "description": "Admin role"},
    {"name": "Recursos Humanos", "description": "RH role"},
    {"name": "Finanzas", "description": ""},
    {"name": "Fiscal", "description": ""},
    {"name": "Comercio Exterior", "description": ""},
    {"name": "Legal", "description": ""},
]


async def seed_database(engine):
    """
    Method to seed the database

    """
    logger.info("SQL: Seeding database")
    async with engine.begin() as conn:
        for role in role_data:
            await conn.execute(Role.__table__.insert().values(role))

    logger.info("SQL: Database seeded")
