from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.area_rol import AreaRolType


async def fetch_responsables(bq_client: bigquery.Client):
    """
    Method to fetch all responsables.

    :param bq_client: BigQuery client.
    :return: List of responsables.
    """

    query = "CALL `nifty-jet-448016-c5.CIVA_QAS.GetResponsable`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    responsables = []
    for row in rows:
        responsables.append(
            ResponsableModel(
                ID=row["ID"],
                Nombre=row["Nombre"],
                AreaCode=AreaRolType(row["AreaRol"]),
            )
        )

    return responsables
