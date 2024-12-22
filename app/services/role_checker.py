from fastapi import HTTPException, Depends, status
from app.middleware.authentication import BaseData
from starlette.requests import Request


async def get_current_user(request: Request) -> BaseData:
    user = request.user

    if not user or not isinstance(user, BaseData):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )
    return user


class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: BaseData = Depends(get_current_user)):
        if not hasattr(user, "role"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User role not found",
            )

        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have access to this resource",
            )
