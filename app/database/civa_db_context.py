from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db_session

class DBContext:

    def __init__(self, session: AsyncSession):
        self.session = session

    
    async def fetch_donut_panel(self, date_ini: str, date_end: str, panel_type: str):
        """
        Method to fetch donut panel data.

        :param session: Session to connect to the database.
        :param date_ini: Start date for filtering.
        :param date_end: End date for filtering.
        :param panel_type: Type for filtering.
        :return: List of donut panel data.
        """
        query = text("SELECT * FROM GetDonutPanel(:DateIni, :DateEnd, :Type)")
        result = await self.execute(query, {"DateIni": date_ini, "DateEnd": date_end, "Type": panel_type})
        data = result.fetchall()

        return data
    
    
    async def fetch_expediente_civa(self, date_ini: str, date_end: str):
        """
        Method to fetch expediente civa details.

        :param session: Session to connect to the database.
        :param date_ini: Initial date (format: YYYY-MM-DDTHH:MM:SS).
        :param date_end: End date (format: YYYY-MM-DDTHH:MM:SS).
        :return: List of expediente civa details.
        """
        query = text("SELECT * FROM GetExpedienteCiva(:DateIni, :DateEnd)")
        result = await self.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
        expedientes = result.fetchall()

        return expedientes
    
    async def fetch_notificaciones(self):
        """
        Method to fetch all notifications.

        :param session: Session to connect to the database.
        :return: List of notifications.
        """
        result = await self.execute(text("SELECT * FROM GetNotificaciones()"))
        notificaciones = result.fetchall()

        return notificaciones
    

    async def fetch_requirement_obligation(self, date_ini: str, date_end: str):
        """
        Method to fetch requirement obligations.

        :param session: Session to connect to the database.
        :param date_ini: Start date for the range.
        :param date_end: End date for the range.
        :return: Dictionary with counts of Pendientes, Proximos, and Hallazgos.
        """
        query = text("SELECT * FROM GetRequirementObligation(:DateIni, :DateEnd)")
        result = await self.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
        obligation = result.fetchone()

        return obligation
    

    async def fetch_tareas_responsable(self, date_ini: str, date_end: str):
        """
        Method to fetch tareas responsables.

        :param session: Session to connect to the database.
        :param date_ini: Start date for filtering tasks.
        :param date_end: End date for filtering tasks.
        :return: List of tareas responsables.
        """
        query = text("SELECT * FROM GetTareasResponsable(:DateIni, :DateEnd)")
        result = await self.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
        tareas = result.fetchall()
        
        return tareas


    async def fetch_total_solicitudes_revisor(self, date_ini: str, date_end: str):
        """
        Method to fetch total solicitudes revisor.

        :param session: Session to connect to the database.
        :param date_ini: Start date for filtering.
        :param date_end: End date for filtering.
        :return: Total solicitudes.
        """
        query = text("SELECT * FROM GetTotalSolicitudesRevisor(:DateIni, :DateEnd)")
        result = await self.execute(query, {"DateIni": date_ini, "DateEnd": date_end})
        total = result.fetchone()
        
        return total
    


async def get_civa_db_context(db_session: AsyncSession = Depends(get_db_session)) -> DBContext:
    """
    Dependency to get the database context.
    """
    return DBContext(db_session)