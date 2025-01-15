from app.database.models.models import Base
from config.logger_config import logger
from sqlalchemy import text



procedures = text("""
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
                  
CREATE OR REPLACE FUNCTION GetRequirementObligation(DateIni DATE, DateEnd DATE)
RETURNS TABLE(Pendientes INT, Proximos INT, Hallazgos INT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        COUNT(*) FILTER (WHERE is_aprobado = FALSE AND fecha_vencimiento > CURRENT_DATE) AS Pendientes,
        COUNT(*) FILTER (WHERE fecha_vencimiento BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days') AS Proximos,
        COUNT(*) FILTER (WHERE es_critico = TRUE) AS Hallazgos
    FROM requirements
    WHERE fecha_vencimiento BETWEEN DateIni AND DateEnd;
END;
$$ LANGUAGE plpgsql;
                  
CREATE OR REPLACE FUNCTION GetExpedienteCiva(DateIni TIMESTAMP, DateEnd TIMESTAMP)
RETURNS TABLE(ID INT, Actualizacion TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        id AS ID,
        actualizacion AS Actualizacion
    FROM expedientes_civa
    WHERE actualizacion BETWEEN DateIni AND DateEnd;
END;
$$ LANGUAGE plpgsql;
                  
                  CREATE OR REPLACE FUNCTION GetTotalSolicitudesRevisor(DateIni DATE, DateEnd DATE)
RETURNS TABLE(Solicitudes INT) AS $$
BEGIN
    RETURN QUERY
    SELECT COUNT(*)
    FROM solicitations
    WHERE fecha_revision BETWEEN DateIni AND DateEnd;
END;
$$ LANGUAGE plpgsql;
                  
CREATE OR REPLACE FUNCTION GetNotificaciones()
RETURNS TABLE(
    ID INT,
    Titulo VARCHAR,
    Referencia VARCHAR,
    Estado VARCHAR,
    Descripcion TEXT,
    Fecha TIMESTAMP,
    EsError BOOLEAN
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        n.id AS ID,
        n.title AS Titulo,
        n.id::TEXT AS Referencia,
        n.state AS Estado,
        n.description AS Descripcion,
        n.date AS Fecha,
        n.is_error AS EsError
    FROM notifications n;
""")

async def stored_prcedures_populate(engine):
    """
    Method to populate the database with stored procedures.
    
    """

    logger.info("SQL: Creating stored procedures ...")
    async with engine.begin() as conn:
        await conn.execute(procedures)
        logger.info("SQL: Stored procedures created successfully!!!")
    await engine.dispose()
    logger.info("SQL: Engine disposed")