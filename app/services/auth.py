import jwt

from datetime import datetime, timedelta
from typing import Optional
from config.config import config


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create access token

    Args:
        data (dict): Payload data
        expires_delta (Optional[timedelta], optional): Expiration time. Defaults to None.

    Returns:
        str: Encoded JWT token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> tuple:
    """
    Verify token

    Args:
        token (str): JWT token

    Returns:
        tuple: Payload data
     
    """
    try:
        payload = jwt.decode(
            token,
            config.CIVA_SECRET_KEY,
            algorithms=[config.CIVA_ALGORITHM],
            options={"verify_aud": False}  # Desactiva la validación de "aud"
        )
        return True, payload
    except jwt.ExpiredSignatureError:
        return False, "Token has expired"
    except jwt.InvalidTokenError:
        return False, "Invalid token"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
