import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta
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
from logger_config import logger


class BaseData:
    def __init__(self, user_id: int, role: str, token: str):
        self.id_client_user = user_id
        self.role = role
        self.token = token  # New token returned to the client

    def __str__(self):
        return f"User ID: {self.id_client_user}, Role: {self.role}"


class OneAuthBackend(AuthenticationBackend):
    """Auth Backend para FastAPI con validación de token JWT."""

    def __init__(self, excluded_urls: List[str] = None):
        """
        Args:
            excluded_urls (List[str]): Routes excluded from authentication.

        """
        self.excluded_urls = [] if excluded_urls is None else excluded_urls

    def generate_new_token(self, payload: dict) -> str:
        """
        Generate a new JWT token with an updated expiration time.

        Args:
            payload (dict): JWT payload.
        """
        logger.info("MIDDLEWARE: Generating new token")
        payload["exp"] = datetime.utcnow() + timedelta(
            minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )  # New expiration time
        return jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)

    async def authenticate(self, conn: HTTPConnection) -> Tuple[AuthCredentials, BaseData]:
        """
        Authenticate the request and return the credentials and user.

        Args:
            conn (HTTPConnection): HTTP Connection object.

        """
        logger.info(f"MIDDLEWARE: Authenticating request to {conn.url.path}")
        # Excluded Public Routes
        if conn.url.path in self.excluded_urls:
            return AuthCredentials(scopes=[]), None

        # Authorization Header
        auth_header = conn.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            logger.error("MIDDLEWARE: No token provided in the Authorization header")
            raise AuthenticationError("No token provided in the Authorization header")

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
            # Generate a new token
            new_token = self.generate_new_token(payload)

            # Build BaseData object with new token
            data = BaseData(
                user_id=payload.get("sub"),
                role=payload.get("role"),
                token=new_token,  # Include the new token
            )

            scopes = payload.get("scopes", [])

            logger.info("MIDDLEWARE: Authenticated user successfully")
        except jwt.PyJWTError:
            logger.error(f"MIDDLEWARE: Invalid token provided")
            raise AuthenticationError(f"Invalid token provided")

        return AuthCredentials(scopes=scopes), data


class AuthenticationMiddleware(BaseAuthenticationMiddleware):
    pass
