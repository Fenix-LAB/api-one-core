from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.models import DatosEmpresaSocioAccionistaCaracterModel

async def fetch_caracter_tipos(bq_client: bigquery.Client):
    """
    Method to fetch caracter tipos.

    :param session: Session to connect to the database.
    :return: Caracter tipos.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetCaracterTipos`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    caracter_tipos = []

    for row in rows:
        caracter_tipos.append(DatosEmpresaSocioAccionistaCaracterModel(
            Code=row['Code'],
            Description=row['Description'],
        ))
            

    return caracter_tipos