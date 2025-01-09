from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse
from app.schemas.common.response import ResponsableResponse
from app.schemas.common.request import ResponsableRequest

from app.services.responsable_service import fetch_responsables
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()


@app.post("/GetResponsable")
@inject
async def GetResponsable(
    request: ResponsableRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get all responsables.

    ## REQUEST
    - page
    #### Type: integer
    #### Description: The page number to retrieve. Starts at 1 and increments to access subsequent pages. Each page contains a subset of records determined by page_size.

    - page_size
    #### Type: integer
    #### Description: The number of records to retrieve per page. Limits the results of the query. Must be between 1 and 100 (depending on your validation logic).


    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    page = request.page
    page_size = request.page_size

    try:
        # responsables, total_records = await fetch_responsables(db_session, page, page_size)

        # responsable_responses = [
        #     ResponsableResponse(
        #         id=responsables.id,
        #         name=responsables.name,
        #         area_code=responsables.area_code,
        #     )
        #     for responsables in responsables
        # ]

        # total_pages = (total_records + page_size - 1) // page_size

        return ApiResponse(
            Success=True,
            Message="Ok",
            Data=ListResponse(
                CurrentPage=0,
                PageSize=0,
                TotalPages=0,
                TotalRecords=0,
                Data = [
                    ResponsableResponse(ID=1, Nombre="Responsable 1", AreaCode="Administrador"),
                    ResponsableResponse(ID=2, Nombre="Responsable 2", AreaCode="Fiscal"),
                    ResponsableResponse(ID=3, Nombre="Responsable 3", AreaCode="Legal"),
                    ResponsableResponse(ID=4, Nombre="Responsable 4", AreaCode="Finanzas"),
                    ResponsableResponse(ID=5, Nombre="Responsable 5", AreaCode="Rrhh"),
                    ResponsableResponse(ID=6, Nombre="Responsable 6", AreaCode="Administrador"),
                    ResponsableResponse(ID=7, Nombre="Responsable 7", AreaCode="Legal"),
                    ResponsableResponse(ID=8, Nombre="Responsable 8", AreaCode="Fiscal"),
                    ResponsableResponse(ID=9, Nombre="Responsable 9", AreaCode="Finanzas"),
                    ResponsableResponse(ID=10, Nombre="Responsable 10", AreaCode="Rrhh"),
                ]
                
            ),
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /get_responsable: {e}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )
