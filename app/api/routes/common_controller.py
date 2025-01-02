from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends

from app.schemas.user.request import UserRequest
from app.schemas.generic_response import ApiResponse
from app.schemas.user.response import UserResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.role_checker import RoleChecker, get_current_user
from app.middleware.authentication import BaseData

auth_router = APIRouter()
security = HTTPBearer()


@auth_router.post("/get_responsable")
@inject
async def GetResponsable(
    # request: UserRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get all responsables.

    ## REQUEST
    NONE: No request parameters

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """