from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.dashboard.response import TareaResponsableResponse

async def fetch_tareas_responsable(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch tareas responsables.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering tasks.
    :param date_end: End date for filtering tasks.
    :return: List of tareas responsables.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.getTareasResponsable`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    tareas = []

    for row in rows:
        tareas.append(
            TareaResponsableResponse(
                Area=row["Area"],
                Usuario=row["Usuario"],
                Asignadas=row["Asignadas"],
                Completadas=row["Completadas"],
                RiegoCode=row["RiegoCode"],
            )
        )

    return tareas
