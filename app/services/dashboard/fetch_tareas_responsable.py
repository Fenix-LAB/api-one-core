from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import TareaResponsableResponse

async def fetch_tareas_responsable(session: AsyncSession, date_ini: str, date_end: str):
    """
    Method to fetch tareas responsables.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering tasks.
    :param date_end: End date for filtering tasks.
    :return: List of tareas responsables.
    """
    query = text("SELECT * FROM GetTareasResponsable(:DateIni, :DateEnd)")
    result = await session.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
    tareas = result.fetchall()
    
    return [TareaResponsableResponse(**tarea) for tarea in tareas]
