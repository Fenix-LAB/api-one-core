from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends

from app.api.schemas.user.request import UserRequest
from app.api.schemas.generic_response import ApiResponse
from app.api.schemas.user.response import UserResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.api.services.role_checker import RoleChecker, get_current_user
from app.middleware.authentication import BaseData

auth_router = APIRouter()
security = HTTPBearer()


@auth_router.post("/user/create")
@inject
async def Create(
    request: UserRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user)
):
    """
    ## DESCRIPTION
    ### Endpoint to create a new user.

    ## REQUEST
    - name: str (User name)
    - email: str (User email)
    - first_name: str (User first name)
    - last_name: str (User last name)
    - password: str (User password)

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    return ApiResponse[UserResponse](Data=UserResponse(**request.dict()), Message="User created successfully", Status="200", Token=user_data.token)
    
