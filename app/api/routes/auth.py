from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse

from app.api.schemas.auth.request import (
    RefreshTokenRequest,
    VerifyTokenRequest,
)
from app.api.schemas.auth.response import RefreshTokenResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.middleware.authentication import OneAuthBackend
# from app.auth.domain.usecase.jwt import JwtUseCase
# from app.container import Container

auth_router = APIRouter()
security = HTTPBearer()


@auth_router.post("/auth/login")
@inject
async def verify_token(
    request: VerifyTokenRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    # usecase: JwtUseCase = Depends(Provide[Container.jwt_service]),
):
    # await usecase.verify_token(token=request.token)
    # return Response(status_code=200)

    print("verify_token")
    return JSONResponse(status_code=200, content="verify_token")


@auth_router.post(
    "/auth/refresh",
    response_model=RefreshTokenResponse,
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