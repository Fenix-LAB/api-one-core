from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.dashboard.response import DonutPanelResponse

async def fetch_donut_panel(bq_client: bigquery.Client, date_ini: str, date_end: str, panel_type: str):
    """
    Method to fetch donut panel data.

    :param session: Session to connect to the database.
    :param date_ini: Start date for filtering.
    :param date_end: End date for filtering.
    :param panel_type: Type for filtering.
    :return: List of donut panel data.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.getDonutPanel`('{date_ini}', '{date_end}', '{panel_type}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    data = []

    for row in rows:
        data.append(
            DonutPanelResponse(
                Porcentaje=row["Porcentaje"],
                Cantidad=row["Cantidad"],
            )
        )

    return data