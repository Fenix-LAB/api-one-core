from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.dashboard.response import ExpedienteCivaResponse

async def fetch_expediente_civa(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch expediente civa details.

    :param session: Session to connect to the database.
    :param date_ini: Initial date (format: YYYY-MM-DDTHH:MM:SS).
    :param date_end: End date (format: YYYY-MM-DDTHH:MM:SS).
    :return: List of expediente civa details.
    """

    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetExpedienteCiva`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    expedientes = []
    
    for row in rows:
        expedientes.append(
            ExpedienteCivaResponse(
                Actualizacion=row['Actualizacion'],
            )
        )
