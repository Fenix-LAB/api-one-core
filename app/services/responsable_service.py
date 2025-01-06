from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# from sqlalchemy.orm import selectinload
from app.database.models.responsable import Responsable
from sqlalchemy.sql import func


async def fetch_responsables(session: AsyncSession, page: int, page_size: int):
    """
    Fetches

    :param session: AsyncSession
    :param page: int
    :param page_size: int
    :return: Tuple[List[Responsable], int]
    """

    offset = (page - 1) * page_size

    # query = select(Responsable).options(selectinload(Responsable.id)).offset(offset).limit(page_size)
    query = select(Responsable).offset(offset).limit(page_size)
    result = await session.execute(query)
    users = result.scalars().all()

    total_records = await session.scalar(select(func.count()).select_from(Responsable))

    return users, total_records
