from fastapi import APIRouter, status

from .routes import login

router = APIRouter()

router.include_router(login.router, tags=["login"])
