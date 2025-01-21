from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import SolicitudesSectionRequerimientosOptionResponse

async def get_solicitudes_section_list(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch solicitudes section list.

    :param session: Session to connect to the database.
    :param date_ini: Start date for the range.
    :param date_end: End date for the range.
    :return: List of solicitudes section.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetSolicitudesSectionList`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    solicitudes_section = []

    for row in rows:
        solicitudes_section.append(
            SolicitudesSectionRequerimientosOptionResponse(
                Code=row['Code'],
                Cantidad=row['Cantidad'],
                Total=row['Total'],
                CantidadSolicitudes=row['CantidadSolicitudes'],
            )
        )

    return solicitudes_section