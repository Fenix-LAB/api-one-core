from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import TotalSolicitudesRevisorResponse

async def fetch_total_solicitudes_revisor(session: AsyncSession, date_ini: str, date_end: str):
    """
    Method to fetch total solicitudes revisor.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering.
    :param date_end: End date for filtering.
    :return: Total solicitudes.
    """
    query = text("SELECT * FROM GetTotalSolicitudesRevisor(:DateIni, :DateEnd)")
    result = await session.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
    total = result.fetchone()
    
    return TotalSolicitudesRevisorResponse(**total)
