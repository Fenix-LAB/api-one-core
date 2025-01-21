from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.models import PaisModel

async def fetch_paises(bq_client: bigquery.Client):
    """
    Method to fetch paises.

    :param session: Session to connect to the database.
    :return: Paises.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetPaises`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    paises = []

    for row in rows:
        paises.append(PaisModel(
            PaisCode=row['PaisCode'],
            TelefonoCode=row['TelefonoCode'],
        ))
            

    return paises