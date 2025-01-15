from app.database.models.models import Base
from config.logger_config import logger
from sqlalchemy import text



get_responsable = text("""
CREATE OR REPLACE FUNCTION GetResponsables()
RETURNS TABLE(ID INT, Nombre VARCHAR, AreaCode VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        r.id AS ID,
        r.name AS Nombre,
        a.name AS AreaCode
    FROM responsables r
    INNER JOIN areas a ON r.area_id = a.id;
END;
$$ LANGUAGE plpgsql;
""")

async def stored_prcedures_populate(engine):
    """
    Method to populate the database with stored procedures.
    
    """

    logger.info("SQL: Creating stored procedures ...")
    async with engine.begin() as conn:
        await conn.execute(get_responsable)
        logger.info("SQL: Stored procedures created successfully!!!")
    await engine.dispose()
    logger.info("SQL: Engine disposed")