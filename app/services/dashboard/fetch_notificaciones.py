from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.dashboard.response import NotificationResponse

async def fetch_notificaciones(session: AsyncSession):
    """
    Method to fetch all notifications.

    :param session: Session to connect to the database.
    :return: List of notifications.
    """
    result = await session.execute(text("SELECT * FROM GetNotificaciones()"))
    notificaciones = result.fetchall()
    return [NotificationResponse(**notificacion) for notificacion in notificaciones]
