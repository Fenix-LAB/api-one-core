from fastapi import APIRouter

from .routes import (
    auth,
    dashboard_controller,
)

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
router.include_router(dashboard_controller.app, tags=["dashboard_controller"])
