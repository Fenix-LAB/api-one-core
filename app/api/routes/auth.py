from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from app.api.schemas.auth.request import (
    RefreshTokenRequest,
    LoginTokenRequest
)
from app.api.schemas.generic_response import ApiResponse
from app.api.schemas.auth.response import LoginResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.middleware.authentication import OneAuthBackend
from app.api.services.auth import create_access_token, verify_token
# from app.auth.domain.usecase.jwt import JwtUseCase
# from app.container import Container

auth_router = APIRouter()
security = HTTPBearer()


@auth_router.post("/auth/login")
@inject
async def Login(
    request: LoginTokenRequest,
    # credentials: HTTPAuthorizationCredentials = Depends(security),
    # usecase: JwtUseCase = Depends(Provide[Container.jwt_service]),
    # allow: roles = Depends(allowroles(["admin", "legal", "RH"])
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
    #  decoded_token = await verify_token(token=request.token)

    # id_usuario_clente

    # Consultar usuario en base de datos (obetener roles)

    # id_usuario_clente, role [admin, legal, RH, etc], tiempo de expiración

    token = create_access_token(data={"sub": 1, "username": "test"})

    return ApiResponse[LoginResponse](Data=LoginResponse(Token=token), Message="Login successful", Status="200", Token=token)


@auth_router.post(
    "/auth/refresh",
    # response_model=RefreshTokenResponse,
)
@inject
async def refresh_token(
    request: RefreshTokenRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    # usecase: JwtUseCase = Depends(Provide[Container.jwt_service]),
):
    # token = await usecase.create_refresh_token(
    #     token=request.token, refresh_token=request.refresh_token
    # )
    # return {"token": token.token, "refresh_token": token.refresh_token}
    print("refresh_token")
    # return {"token": "123", "refresh": "54"}
    return JSONResponse(status_code=200, content="refresh_token")