from app.database.models.models import Base
from config.logger_config import logger
from sqlalchemy import text



procedures = [
    text(
    """
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
    """),

    text(
    """        
    CREATE OR REPLACE FUNCTION GetRequirementObligation(DateIni DATE, DateEnd DATE)
    RETURNS TABLE(Pendientes BIGINT, Proximos BIGINT, Hallazgos BIGINT) AS $$
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
    """),

    text(
    """           
    CREATE OR REPLACE FUNCTION GetExpedienteCiva(DateIni DATE, DateEnd DATE)
    RETURNS TABLE(ID INT, Actualizacion TIMESTAMP) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            expedientes_civa.id AS ID,
            expedientes_civa.actualizacion AS Actualizacion
        FROM expedientes_civa
        WHERE expedientes_civa.actualizacion::DATE BETWEEN DateIni AND DateEnd;
    END;
    $$ LANGUAGE plpgsql;
    """),

    text(
    """           
    CREATE OR REPLACE FUNCTION GetTotalSolicitudesRevisor(DateIni DATE, DateEnd DATE)
    RETURNS TABLE(Solicitudes BIGINT) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            COUNT(*) AS Solicitudes
        FROM solicitudes_revisor
        WHERE fecha BETWEEN DateIni AND DateEnd;
    END;
    $$ LANGUAGE plpgsql;
    """),

    text(
    """                    
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
    END;
    $$ LANGUAGE plpgsql;
    """),

    text(
    """                
    CREATE OR REPLACE FUNCTION GetDonutPanel(DateIni TIMESTAMP, DateEnd TIMESTAMP, Type VARCHAR)
    RETURNS TABLE(ColorCode VARCHAR, NombreCode VARCHAR, Porcentaje INT, Cantidad INT) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            CASE 
                WHEN r.is_aprobado THEN 'Green'
                ELSE 'Red'
            END AS ColorCode,
            CASE 
                WHEN r.is_aprobado THEN 'Completado'
                ELSE 'Pendiente'
            END AS NombreCode,
            COUNT(r.id) * 100 / NULLIF(SUM(COUNT(r.id)) OVER (), 0) AS Porcentaje,
            COUNT(r.id) AS Cantidad
        FROM requirements r
        WHERE r.fecha_inicio BETWEEN DateIni AND DateEnd
        AND r.comentarios LIKE '%' || Type || '%'
        GROUP BY r.is_aprobado;
    END;
    $$ LANGUAGE plpgsql;
    """),

    text(
    """                 
    CREATE OR REPLACE FUNCTION GetTareasResponsable(DateIni DATE, DateEnd DATE)
    RETURNS TABLE(Area VARCHAR, Usuario VARCHAR, Asignadas INT, Completadas INT, RiesgoCode VARCHAR) AS $$
    BEGIN
        RETURN QUERY
        SELECT 
            a.name AS Area,
            u.username AS Usuario,
            COUNT(r.id) AS Asignadas,
            COUNT(CASE WHEN r.is_aprobado THEN 1 END) AS Completadas,
            CASE 
                WHEN COUNT(CASE WHEN r.is_aprobado THEN 1 END) < COUNT(r.id) THEN 'Alto'
                ELSE 'Medio'
            END AS RiesgoCode
        FROM responsables r
        INNER JOIN areas a ON r.area_id = a.id
        INNER JOIN user_roles ur ON ur.user_id = r.id
        INNER JOIN users u ON u.id = ur.user_id
        WHERE r.fecha_envio BETWEEN DateIni AND DateEnd
        GROUP BY a.name, u.username;
    END;
    $$ LANGUAGE plpgsql;
    """
    )
]

async def stored_prcedures_populate(engine):
    """
    Method to populate the database with stored procedures.
    
    """

    logger.info("SQL: Creating stored procedures ...")
    async with engine.begin() as conn:
        for procedure in procedures:
            try:
                await conn.execute(procedure)
                logger.info("SQL: Stored procedure created successfully.")
            except Exception as e:
                logger.error(f"SQL: Error creating stored procedure: {e}")
    await engine.dispose()
    logger.info("SQL: Engine disposed")


async def drop_procedures(engine):
    """
    Method to drop the stored procedures.
    """
    function_definitions = [
        "GetResponsables()",
        "GetRequirementObligation(DATE, DATE)",
        "GetExpedienteCiva(TIMESTAMP, TIMESTAMP)",
        "GetTotalSolicitudesRevisor(DATE, DATE)",
        "GetNotificaciones()",
        "GetDonutPanel(TIMESTAMP, TIMESTAMP, VARCHAR)",
        "GetTareasResponsable(DATE, DATE)"
    ]

    logger.info("SQL: Dropping stored procedures ...")
    async with engine.begin() as conn:
        for function_name in function_definitions:
            query = text(f"DROP FUNCTION IF EXISTS {function_name} CASCADE;")
            try:
                await conn.execute(query)
                logger.info(f"SQL: Stored procedure {function_name} dropped successfully.")
            except Exception as e:
                logger.error(f"SQL: Error dropping stored procedure {function_name}: {e}")

    await engine.dispose()
    logger.info("SQL: Engine disposed")
