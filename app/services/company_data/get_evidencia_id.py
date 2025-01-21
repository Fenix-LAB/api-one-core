from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import DatosEmpresaEvidenciaResponse
from app.schemas.models import AreaRolModel
from app.schemas.models import ResponsableModel

async def fetch_evidencia_id(bq_client: bigquery.Client, id: int, code_section: str):
    """
    Method to fetch evidencia id.

    :param session: Session to connect to the database.
    :param id: Id.
    :param code_section: Code section.
    :return: Evidencia id.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetEvidenciaId`({id}, '{code_section}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    evidencia_id = []

    for row in rows:
        evidencia_id.append(DatosEmpresaEvidenciaResponse(
            ID=row['ID'],
            CaseNumber=row['CaseNumber'],
            AreaRols=AreaRolModel(
                Code=row['AreaRols_Code'],
                Name=row['AreaRols_Name'],
            ),
            Responsables=ResponsableModel(
                ID=row['Responsables_ID'],
                Nombre=row['Responsables_Nombre'],
                AreaCode=row['Responsables_AreaCode'],
            ),
            Cliente=row['Cliente'],
            Fecha=row['Fecha'],
            Recomendaciones=row['Recomendaciones'],
            Hallazgo=row['Hallazgo'],
        ))
            

    return evidencia_id