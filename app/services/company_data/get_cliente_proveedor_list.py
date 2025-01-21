from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import HistoricoResponse
from app.schemas.company_data.response import ClienteProveedorResponse

async def fetch_cliente_proveedor_list(bq_client: bigquery.Client):
    """
    Method to fetch cliente proveedor list.

    :param session: Session to connect to the database.
    :return: Cliente proveedor list.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetClienteProveedorList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    cliente_proveedor_list = []

    for row in rows:
        cliente_proveedor_list.append(HistoricoResponse(
            Status=row['Status'],
            Usuario=row['Usuario'],
            Fecha=row['Fecha'],
            Data=ClienteProveedorResponse(
                ID=row['Data']['ID'],
                CaseNumber=row['Data']['CaseNumber'],
                IsCompany=row['Data']['IsCompany'],
                Name=row['Data']['Name'],
                Tipo=row['Data']['Tipo'],
                ApellidoPaterno=row['Data']['ApellidoPaterno'],
                ApellidoMaterno=row['Data']['ApellidoMaterno'],
                TipoMovimiento=row['Data']['TipoMovimiento'],
                Aviso=row['Data']['Aviso'],
                Municipio=row['Data']['Municipio'],
                EstadoCode=row['Data']['EstadoCode'],
                EstadoNombre=row['Data']['EstadoNombre'],
                PaisCode=row['Data']['PaisCode'],
                FechaMovimiento=row['Data']['FechaMovimiento'],
        ))
    )
            

    return cliente_proveedor_list