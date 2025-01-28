from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.area_rol import AreaRolType
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
    - Empty request.

    ## RESPONSE
    - Data: List of responsables.

    """

    try:

        logger.info(f"ENDPOINT /GetResponsable: request={request.dict()}")

        logger.info(f"ENDPOINT /GetResponsable: Trying to get responsables ...")

        data = await fetch_responsables(db_session)

        logger.info(f"ENDPOINT /get_responsable: data={data}")

        return ApiResponse(
            Success=True,
            Message="Ok",
            Data=ListResponse(
                CurrentPage=0,
                PageSize=0,
                TotalPages=0,
                TotalRecords=0,
                Data = data
                
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
