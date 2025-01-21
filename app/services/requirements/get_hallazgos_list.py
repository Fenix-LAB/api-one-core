from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.models import HallazgoOptionModel

async def get_hallazgos_list(bq_client: bigquery.Client, code_section: str):
    """
    Method to fetch hallazgos list.

    :param session: Session to connect to the database.
    :param code_section: Requerimientos section option code.
    :return: List of hallazgos.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetHallazgosList`('{code_section}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    hallazgos = []

    for row in rows:
        hallazgos.append(
            HallazgoOptionModel(
                ID=row['ID'],
                Code=row['Code'],
                Nombre=row['Nombre']
            )
        )

    return hallazgos