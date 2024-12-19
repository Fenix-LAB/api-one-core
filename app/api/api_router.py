from fastapi import APIRouter, status

from .routes import auth, users

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
router.include_router(users.auth_router, tags=["users"])
