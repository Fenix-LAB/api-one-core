from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from config.logger_config import logger
from config.config import config

from app.api.api_router import router

from app.database.session import engine
from app.database.seeder import seed_database
from app.database.populate import create_tables
from app.database.procedures.stores_procedures import stored_prcedures_populate, drop_procedures

from app.middleware import (
    OneAuthBackend,
    AuthenticationMiddleware,
)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router, prefix=config.ROUTE_PATH)
    # Add more routers here


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
        ),
        # Add more middleware here
    ]
    return middleware


def create_app() -> FastAPI:
    """
    Method to create the FastAPI application.
    
    """

    logger.info(f"SERVER: Application One Core - env: {config.ENV}")
    app_ = FastAPI(
        title="one-core",
        description="One Core API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        middleware=make_middleware(),
    )

    init_routers(app_=app_)
    logger.info("SERVER: Routers initialized")

    @app_.on_event("startup")
    async def on_startup():
        """
        Method to execute actions on application startup.
        Only executed in development environment.
        
        """

        if config.ENV == "production":
            logger.info("SERVER: Production environment, skipping 'on_startup' event")
            return
        
        # await create_tables(engine)
        # await seed_database(engine)
        # await drop_procedures(engine)
        # await stored_prcedures_populate(engine)
        # Add more actions here

        logger.info("SERVER: On startup event completed")

    logger.info("SERVER: App lunch completed")

    return app_


app = create_app()
