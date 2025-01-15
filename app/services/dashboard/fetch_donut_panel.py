from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import DonutPanelResponse

async def fetch_donut_panel(session: AsyncSession, date_ini: str, date_end: str, panel_type: str):
    """
    Method to fetch donut panel data.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering.
    :param date_end: End date for filtering.
    :param panel_type: Type for filtering.
    :return: List of donut panel data.
    """
    query = text("SELECT * FROM GetDonutPanel(:DateIni, :DateEnd, :Type)")
    result = await session.execute(query, {"DateIni": date_ini, "DateEnd": date_end, "Type": panel_type})
    data = result.fetchall()

    return [DonutPanelResponse(**item) for item in data]
