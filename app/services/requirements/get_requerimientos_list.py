from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import RequerimientoElementResponse

async def get_requerimientos_list(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch requirement obligations.

    :param session: Session to connect to the database.
    :param date_ini: Start date for the range.
    :param date_end: End date for the range.
    :return: Dictionary with counts of Pendientes, Proximos, and Hallazgos.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetRequerimientoElementos`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    obligation = []

    for row in rows:
        obligation.append(
            RequerimientoElementResponse(
                ID=row['ID'],
                Verificacion=row['Verificacion'],
                Usuario=row['Usuario'],
                Elementos=row['Elementos'],
                Vencimiento=row['Vencimiento'],
                EsCritico=row['EsCritico'],
                FechaEnvio=row['FechaEnvio'],
            )
        )
    return obligation