from fastapi import APIRouter, status

from .routes import auth

router = APIRouter()

router.include_router(auth.auth_router, tags=["auth"])
