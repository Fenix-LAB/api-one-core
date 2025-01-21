from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import SectionOptionRequerimientosResponse

async def fetch_section_list(bq_client: bigquery.Client, date_ini: str, date_end: str):
    """
    Method to fetch section list.

    :param session: Session to connect to the database.
    :param date_ini: Start date.
    :param date_end: End date.
    :return: Section list.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetSectionList`('{date_ini}', '{date_end}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    section_list = []

    for row in rows:
        section_list.append(SectionOptionRequerimientosResponse(
            Code=row['Code'],
            Cantidad=row['Cantidad'],
            Total=row['Total'],
            ProximosVencer=row['ProximosVencer'],
            Selected=row['Selected'],
            Enable=row['Enable'],
        ))
            

    return section_list