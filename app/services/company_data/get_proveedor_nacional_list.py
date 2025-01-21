from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import ProveedorNacionalResponse

async def fetch_proveedor_nacional_list(bq_client: bigquery.Client):
    """
    Method to fetch proveedor nacional list.

    :param session: Session to connect to the database.
    :return: Proveedor nacional list.
    """
    
    query = "CALL `nifty-jet-448016-c5.CIVA_QAS.GetProveedorNacionalList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    proveedor_nacional_list = []

    for row in rows:
        proveedor_nacional_list.append(ProveedorNacionalResponse(
            ID=row['ID'],
            CaseNumber=row['CaseNumber'],
            RFC=row['RFC'],
            ValorOperaciones=row['ValorOperaciones'],
            Porcentaje=row['Porcentaje'],
            IsOpinionPositiva=row['IsOpinionPositiva'],
            IsOperacionesVirtuales=row['IsOperacionesVirtuales'],
            FechaMovimiento=row['FechaMovimiento'],
            Aviso=row['Aviso'],
            FechaAviso=row['FechaAviso'],
        ))
            

    return proveedor_nacional_list