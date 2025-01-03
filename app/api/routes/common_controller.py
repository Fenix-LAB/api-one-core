from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse
from app.schemas.responsable.response import ResponsableResponse
from app.schemas.responsable.request import ResponsableRequest

from app.services.responsable_service import fetch_responsables
from app.services.role_checker import RoleChecker, get_current_user


app = APIRouter()
security = HTTPBearer()


@app.post("/get_responsable")
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
    ### page
    #### Type: integer
    #### Description: The page number to retrieve. Starts at 1 and increments to access subsequent pages. Each page contains a subset of records determined by page_size.

    ### page_size
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
        responsables, total_records = await fetch_responsables(db_session, page, page_size)

        responsable_responses = [
            ResponsableResponse(
                id=responsables.id,
                name=responsables.name,
                area_code=responsables.area_code,
            )
            for responsables in responsables
        ]

        total_pages = (total_records + page_size - 1) // page_size

        return ApiResponse(
            Status='200',
            Message="Success",
            Data=ListResponse(
                current_page=page,
                page_size=page_size,
                total_pages=total_pages,
                total_records=total_records,
                data=responsable_responses,
            ),
            Token=user_data.token,
        )
    
    except Exception:
        return ApiResponse(
            Status='500',
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )
