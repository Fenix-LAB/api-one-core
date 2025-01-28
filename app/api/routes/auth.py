from fastapi import APIRouter
from dependency_injector.wiring import inject
from app.schemas.auth.request import LoginTokenRequest
from app.schemas.generic_response import ApiResponseNoToken
from app.schemas.auth.response import LoginResponse
from app.services.auth import create_access_token, verify_token

auth_router = APIRouter()


@auth_router.post("/login")
@inject
async def Login(
    request: LoginTokenRequest,
):
    """
    ## DESCRIPTION
    ### Endpoint to login, in order to get a JWT token is necessary provide a valid JWT token (from main backend).

    ## REQUEST
    - token: str (JWT token)

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """
    # decoded_token = await verify_token(token=request.token)

    # id_usuario_clente

    # Consultar usuario en base de datos (obetener roles)

    # id_usuario_clente, role [admin, legal, RH, etc], tiempo de expiración

    token = create_access_token(data={"sub": "1", "role": "admin"})
    return ApiResponseNoToken[LoginResponse](
        Data=LoginResponse(Token=token), Message="Login successful", Success=True
    )
