from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.schemas.generic_response import ApiResponse
from app.schemas.common.request import ResponsableRequest

from app.services.common.responsable_service import fetch_responsables
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()


@app.post("/GetResponsable")
@inject
async def GetResponsable(
    request: ResponsableRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

        data, token = await fetch_responsables(
            token=user_data.token
        )

        if data is None:
            return ApiResponse(
                success="500",
                message="Internal Server Error",
                data=None,
                token=token,
            )
        
        return ApiResponse(
            success=True,
            message="Success",
            data=data,
            token=token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /get_responsable: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )