import jwt
from jwt import PyJWTError
from typing import List, Tuple
from starlette.middleware.authentication import AuthenticationError
from starlette.requests import HTTPConnection
from starlette.authentication import (
    AuthenticationBackend,
    AuthCredentials,
)
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)

from config.config import config


class BaseUser:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username

    def __str__(self):
        return self.username


class OneAuthBackend(AuthenticationBackend):
    """Auth Backend para FastAPI con validación de token JWT."""

    def __init__(self, excluded_urls: List[str] = None):
        """
        Args:
            excluded_urls (List[str]): Routes excluded from authentication.
        
        """
        self.excluded_urls = [] if excluded_urls is None else excluded_urls

    async def authenticate(self, conn: HTTPConnection) -> Tuple[AuthCredentials, BaseUser]:
        """
        Authenticate the request and return the credentials and user.

        Args:
            conn (HTTPConnection): HTTP Connection object.

        """
        # Excluded Public Routes
        if conn.url.path in self.excluded_urls:
            print(f'Excluded URL: {conn.url.path}')
            return AuthCredentials(scopes=[]), None

        # Authorization Header
        auth_header = conn.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise AuthenticationError("No token provided in the Authorization header")

        token = auth_header.split(" ")[1]

        try:
            print(f'Token: {token}')
            payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
            user = BaseUser(user_id=payload.get("sub"), username=payload.get("username"))
            scopes = payload.get("scopes", []) 
        except PyJWTError:
            raise AuthenticationError("Invalid token provided")

        return AuthCredentials(scopes=scopes), user
    

class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass