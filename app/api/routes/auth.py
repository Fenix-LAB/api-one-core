from fastapi import APIRouter
from dependency_injector.wiring import inject
from app.schemas.auth.request import LoginTokenRequest
from app.schemas.generic_response import ApiResponseNoToken
from app.schemas.auth.response import LoginResponse
from app.services.auth import login_service

from config.logger_config import logger

auth_router = APIRouter()


@auth_router.post("/Account/login")
@inject
async def Login(
    request: LoginTokenRequest,
):
    """
    ## DESCRIPTION
    ### Endpoint to login, in order to get a JWT token is necessary provide a valid JWT token (from main project).

    ## REQUEST
    - token: str (JWT token)

    ## RESPONSE
        {
        "Success": Bool,
        "Message": "str",
        "Data": {
            "Token": "str"
            }
        }

    """

    # Call login service
    login_response = await login_service(request.token)

    if login_response.get("success") is False:
        logger.error("LOGIN: Login failed")
        return ApiResponseNoToken[LoginResponse](
            Data=LoginResponse(Token="Error authenticating"),
            Message="Login failed",
            Success=False,
        )

    logger.info("LOGIN: Login successful")

    return ApiResponseNoToken[LoginResponse](
        Data=LoginResponse(Token=login_response.get("data")), Message="Login successful", Success=True
    )
