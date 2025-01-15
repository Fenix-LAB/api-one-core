from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.schemas.models.area_rol import AreaRolType


async def fetch_responsables(session: AsyncSession):
    """
    Method to fetch all responsables.

    :param session: Session to connect to the database.
    :return: List of responsables.
    """

    result = await session.execute(text("SELECT * FROM GetResponsables()"))
    responsables = result.fetchall()
    return [
        {
            "ID": responsable[0],
            "Nombre": responsable[1],
            "AreaCode": AreaRolType[responsable[2]],
        }
        for responsable in responsables
    ]