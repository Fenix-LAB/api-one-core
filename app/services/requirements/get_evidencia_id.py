from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.requirements.response import RequerimientosEvidenciaResponse
from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.file_info import FileInfoModel

async def fetch_evidencia_id(bq_client: bigquery.Client, id: str, code_section: str):
    """
    Method to fetch requirement evidences.

    :param session: Session to connect to the database.
    :param date_ini: Start date for the range.
    :param date_end: End date for the range.
    :return: Dictionary with counts of Pendientes, Proximos, and Hallazgos.
    """
    
    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetRequerimientoEvidencia`('{id}', '{code_section}')"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    evidencia = []

    for row in rows:
        evidencia.append(
            RequerimientosEvidenciaResponse(
                ID=row['ID'],
                Elemento=row['Elemento'],
                CaseNumber=row['CaseNumber'],
                Status=row['Status'],
                FechaInicio=row['FechaInicio'],
                FechaVencimiento=row['FechaVencimiento'],
                ProximoVencer=row['ProximoVencer'],
                AreaRols=AreaRolModel(**row['AreaRols']),
                Responsables=ResponsableModel(**row['Responsables']),
                Archivos=FileInfoModel(**row['Archivos']),
                Ubicacion=row['Ubicacion'],
                Comentarios=row['Comentarios'],
                HallazgoComentarios=row['HallazgoComentarios'],
                HallazgoRecomendaciones=row['HallazgoRecomendaciones']
            )
        )

    return evidencia