from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.dashboard.response import NotificationResponse

async def fetch_notificaciones(bq_client: bigquery.Client):
    """
    Method to fetch all notifications.

    :param session: Session to connect to the database.
    :return: List of notifications.
    """
    
    query = "CALL `nifty-jet-448016-c5.CIVA_QAS.getNotificaciones`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    notifications = []

    for row in rows:
        notifications.append(
            NotificationResponse(
                ID=row["ID"],
                Titulo=row["Titulo"],
                Descripcion=row["Descripcion"],
                Referencia=row["Referencia"],
                Estado=row["Estado"],
                Fecha=row["Fecha"],
                EsError=row["EsError"],
            )
        )

    return notifications
