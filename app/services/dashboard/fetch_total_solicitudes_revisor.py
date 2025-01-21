from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.dashboard.response import TotalSolicitudesRevisorResponse

async def fetch_total_solicitudes_revisor(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch total solicitudes revisor.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering.
    :param date_end: End date for filtering.
    :return: Total solicitudes.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.getTotalSolicitudesRevisor`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    solicitudes = []

    for row in rows:
        solicitudes.append(
            TotalSolicitudesRevisorResponse(
                Solicitudes=row["Solicitudes"],
            )
        )

    return solicitudes
