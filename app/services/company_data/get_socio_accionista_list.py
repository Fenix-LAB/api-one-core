from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import HistoricoResponse, SocioAccionistaResponse

async def fetch_socio_accionista_list(bq_client: bigquery.Client):
    """
    Method to fetch socio accionista list.

    :param session: Session to connect to the database.
    :return: Socio accionista list.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetSocioAccionistaList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    socio_accionista_list = []

    for row in rows:
        socio_accionista_list.append(HistoricoResponse(
            Status=row['Status'],
            Usuario=row['Usuario'],
            Fecha=row['Fecha'],
            Data=SocioAccionistaResponse(
                ID=row['ID'],
                CaseNumber=row['CaseNumber'],
                RFC=row['RFC'],
                CaracterCode=row['CaracterCode'],
                CaracterDescripcion=row['CaracterDescripcion'],
                TipoMovimiento=row['TipoMovimiento'],
                EscrituraPublica=row['EscrituraPublica'],
                FechaEscritura=row['FechaEscritura'],
                IsCompany=row['IsCompany'],
                IsObligadoTributar=row['IsObligadoTributar'],
                Nombre=row['Nombre'],
                NombreEmpresa=row['NombreEmpresa'],
        ))
        )
            

    return socio_accionista_list