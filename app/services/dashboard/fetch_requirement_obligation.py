from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import RequerimientoObligacionesResponse

async def fetch_requirement_obligation(session: AsyncSession, date_ini: str, date_end: str):
    """
    Method to fetch requirement obligations.

    :param session: Session to connect to the database.
    :param date_ini: Start date for the range.
    :param date_end: End date for the range.
    :return: Dictionary with counts of Pendientes, Proximos, and Hallazgos.
    """
    query = text("SELECT * FROM GetRequirementObligation(:DateIni, :DateEnd)")
    result = await session.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
    obligation = result.fetchone()

    return RequerimientoObligacionesResponse(
        Pendientes=obligation.Pendientes,
        Proximos=obligation.Proximos,
        Hallazgos=obligation.Hallazgos,
    )