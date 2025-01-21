from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import LegalUsoResponse, HistoricoResponse
from app.schemas.models import DatosEmpresaLegalUsoModel

async def fetch_legal_uso_list(bq_client: bigquery.Client):
    """
    Method to fetch legal uso list.

    :param session: Session to connect to the database.
    :return: Legal uso list.
    """
    
    query = "CALL `nifty-jet-448016-c5.CIVA_QAS.GetLegalUsoList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    legal_uso_list = []

    for row in rows:
        legal_uso_list.append(HistoricoResponse(
            Status=row['Status'],
            Usuario=row['Usuario'],
            Fecha=row['Fecha'],
            Data=LegalUsoResponse(
                ID=row['Data']['ID'],
                CaseNumber=row['Data']['CaseNumber'],
                DomicilioAcreditacion=DatosEmpresaLegalUsoModel(
                    Calle=row['Data']['DomicilioAcreditacion']['Calle'],
                    Colonia=row['Data']['DomicilioAcreditacion']['Colonia'],
                    CP=row['Data']['DomicilioAcreditacion']['CP'],
                    Municipio=row['Data']['DomicilioAcreditacion']['Municipio'],
                    EstadoCode=row['Data']['DomicilioAcreditacion']['EstadoCode'],
                    EstadoNombre=row['Data']['DomicilioAcreditacion']['EstadoNombre'],
                    PaisCode=row['Data']['DomicilioAcreditacion']['PaisCode'],
                    Localidad=row['Data']['DomicilioAcreditacion']['Localidad'],
                    NumeroExterior=row['Data']['DomicilioAcreditacion']['NumeroExterior'],
                    NumeroInterior=row['Data']['DomicilioAcreditacion']['NumeroInterior'],
                    FechaInicioVigencia=row['Data']['DomicilioAcreditacion']['FechaInicioVigencia'],
                ),
                DomicilioNuevo=DatosEmpresaLegalUsoModel(
                    Calle=row['Data']['DomicilioNuevo']['Calle'],
                    Colonia=row['Data']['DomicilioNuevo']['Colonia'],
                    CP=row['Data']['DomicilioNuevo']['CP'],
                    Municipio=row['Data']['DomicilioNuevo']['Municipio'],
                    EstadoCode=row['Data']['DomicilioNuevo']['EstadoCode'],
                    EstadoNombre=row['Data']['DomicilioNuevo']['EstadoNombre'],
                    PaisCode=row['Data']['DomicilioNuevo']['PaisCode'],
                    Localidad=row['Data']['DomicilioNuevo']['Localidad'],
                    NumeroExterior=row['Data']['DomicilioNuevo']['NumeroExterior'],
                    NumeroInterior=row['Data']['DomicilioNuevo']['NumeroInterior'],
                    FechaInicioVigencia=row['Data']['DomicilioNuevo']['FechaInicioVigencia'],
                )
        ))
)
            

    return legal_uso_list