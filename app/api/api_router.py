from fastapi import APIRouter, status

from .routes import auth, common_controller

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
router.include_router(common_controller.app, tags=["common_controller"])
