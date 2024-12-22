from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from logger_config import logger

from config.config import config
from app.api.api_router import router

from app.middleware import (
    OneAuthBackend,
    AuthenticationMiddleware,
    ResponseLogMiddleware,
    # SQLAlchemyMiddleware,
)


def init_routers(app_: FastAPI) -> None:
    # container = Container()
    # user_router.container = container
    # auth_router.container = container
    app_.include_router(router, prefix=config.ROUTE_PATH)
    # app_.include_router(auth_router)


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=OneAuthBackend(excluded_urls=config.EXCLUDED_URLS),
            # on_error=on_auth_error,
        ),
        # Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="one-core",
        description="One Core API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        # dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    logger.info("App created")
    return app_


app = create_app()
