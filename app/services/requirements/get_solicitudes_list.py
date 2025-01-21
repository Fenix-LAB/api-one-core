from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import RequerimientoElementResponse

async def fetch_solicitudes_list(bq_client: bigquery.Client, code: str, date_ini: str, date_end: str):
    """
    Method to fetch solicitudes list.

    :param session: Session to connect to the database.
    :param date_ini: Start date for the range.
    :param date_end: End date for the range.
    :return: List of solicitudes.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetSolicitudesList`('{code}', '{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    solicitudes = []

    for row in rows:
        solicitudes.append(
            RequerimientoElementResponse(
                ID=row['ID'],
                Verificacion=row['Verificacion'],
                Usuario=row['Usuario'],
                Elementos=row['Elementos'],
                Vencimiento=row['Vencimiento'],
            )
        )

    return solicitudes