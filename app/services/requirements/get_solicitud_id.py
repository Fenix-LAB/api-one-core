from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import SolicitudResponse
from app.schemas.models import AreaRolModel
from app.schemas.models import ResponsableModel


async def fetch_solicitud_id(bq_client: bigquery.Client, id: str, code_section: str):
    """
    Method to fetch solicitud by ID.

    :param session: Session to connect to the database.
    :param id: Solicitud ID.
    :param code_section: Requerimientos section option code.
    :return: Solicitud.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetSolicitudId`('{id}', '{code_section}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    solicitud = None

    for row in rows:
        solicitud = SolicitudResponse(
            ID=row['ID'],
            Elemento=row['Elemento'],
            CaseNumber=row['CaseNumber'],
            Cliente=row['Cliente'],
            Status=row['Status'],
            FechaRevision=row['FechaRevision'],
            AreaRols=AreaRolModel(**row['AreaRols']),
            Responsables=ResponsableModel(**row['Responsables']),
        )
            

    return solicitud