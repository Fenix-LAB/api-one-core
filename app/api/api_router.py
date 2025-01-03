from fastapi import APIRouter, status

from .routes import auth, common_controller, dashboard_controller

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
router.include_router(common_controller.app, tags=["common_controller"])
router.include_router(dashboard_controller.app, tags=["dashboard_controller"])
