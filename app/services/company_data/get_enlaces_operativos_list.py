from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import HistoricoResponse, EnlaceOperativoResponse

async def fetch_enlaces_operativos_list(bq_client: bigquery.Client):
    """
    Method to fetch enlaces operativos list.

    :param session: Session to connect to the database.
    :return: Enlaces operativos list.
    """
    
    query = "CALL `nifty-jet-448016-c5.CIVA_QAS.GetEnlacesOperativosList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    enlaces_operativos_list = []

    for row in rows:
        enlaces_operativos_list.append(HistoricoResponse(
            Status=row['Status'],
            Usuario=row['Usuario'],
            Fecha=row['Fecha'],
            Data=EnlaceOperativoResponse(
                ID=row['Data']['ID'],
                CaseNumber=row['Data']['CaseNumber'],
                Nombre=row['Data']['Nombre'],
                RFC=row['Data']['RFC'],
                TipoRelacion=row['Data']['TipoRelacion'],
                FechaInicio=row['Data']['FechaInicio'],
                FechaFin=row['Data']['FechaFin'],
                Observaciones=row['Data']['Observaciones'],
        ))
        )

    return enlaces_operativos_list