from google.cloud import bigquery
from fastapi.concurrency import run_in_threadpool
from app.schemas.company_data.response import HistoricoResponse, RazonSocialResponse


async def fetch_razon_social_historico_list(bq_client: bigquery.Client):
    """
    Method to fetch razon social historico list.

    :param session: Session to connect to the database.
    :return: Razon social historico list.
    """

    query = f"CALL `nifty-jet-448016-c5.CIVA_QAS.GetRazonSocialHistoricoList`()"

    query_job = await run_in_threadpool(bq_client.query, query)
    rows = await run_in_threadpool(query_job.result)

    razon_social_historico_list = []

    for row in rows:
        razon_social_historico_list.append(HistoricoResponse(
            Status=row['Status'],
            Usuario=row['Usuario'],
            Fecha=row['Fecha'],
            Data=RazonSocialResponse(
                ID=row['ID'],
                CaseNumber=row['CaseNumber'],
                Name=row['Name'],
                RFC=row['RFC'],
                Folio=row['Folio'],
                MovementDate=row['MovementDate'],
                DeedDate=row['DeedDate'],
                Fedatario=row['Fedatario'],
                Notary=row['Notary'],
                Notice=row['Notice'],
                NoticeDate=row['NoticeDate'],
                IsCompany=row['IsCompany'],
        ))
    )
            
    return razon_social_historico_list