from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from sqlalchemy.sql import func

from app.database.models.requirement import Requirement
from app.database.models.finding import Finding


async def get_requerimiento_obligaciones(session: AsyncSession):
    # Fecha límite para "próximos"
    now = datetime.now()
    near_future = now + timedelta(days=7)  # Considera próximos a vencerse en 7 días

    # Contar pendientes
    pendientes_query = (
        select(func.count())
        .select_from(Requirement)
        .where(Requirement.verification_status == "Pending")
    )
    pendientes = await session.scalar(pendientes_query)

    # Contar próximos a vencerse
    proximos_query = (
        select(func.count())
        .select_from(Requirement)
        .where(Requirement.due_date <= near_future, Requirement.verification_status == "Pending")
    )
    proximos = await session.scalar(proximos_query)

    # Contar hallazgos
    hallazgos_query = select(func.count()).select_from(Finding)
    hallazgos = await session.scalar(hallazgos_query)

    # Retornar resultados
    return pendientes, proximos, hallazgos
