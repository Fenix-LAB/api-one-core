from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.models import PaisEstadoModel

async def fetch_pais_estados(bq_client: bigquery.Client, pais_code: str):
    """
    Method to fetch pais estados.

    :param session: Session to connect to the database.
    :param pais_code: Pais code.
    :return: Pais estados.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetPaisEstados`('{pais_code}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    pais_estados = []

    for row in rows:
        pais_estados.append(PaisEstadoModel(
            PaisCode=row['PaisCode'],
            EstadoCode=row['EstadoCode'],
            EstadoName=row['EstadoName'],
        ))
            

    return pais_estados