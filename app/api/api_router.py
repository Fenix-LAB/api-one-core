from fastapi import APIRouter, status

from .routes import auth, users, common_controller

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
router.include_router(users.auth_router, tags=["users"])
router.include_router(common_controller.auth_router, tags=["common_controller"])
