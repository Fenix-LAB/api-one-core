from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import ExpedienteCivaResponse

async def fetch_expediente_civa(session: AsyncSession, date_ini: str, date_end: str):
    """
    Method to fetch expediente civa details.

    :param session: Session to connect to the database.
    :param date_ini: Initial date (format: YYYY-MM-DDTHH:MM:SS).
    :param date_end: End date (format: YYYY-MM-DDTHH:MM:SS).
    :return: List of expediente civa details.
    """
    query = text("SELECT * FROM GetExpedienteCiva(:DateIni, :DateEnd)")
    result = await session.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
    expedientes = result.fetchall()

    logger.info(f"Expediente civa details fetched successfully: {expedientes}")

    return [ExpedienteCivaResponse(
        Actualizacion=expediente[0].strftime("%Y-%m-%d %H:%M:%S")
    ) for expediente in expedientes]
        
