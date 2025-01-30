import requests
from config.config import config

async def login_service(token: str) -> dict:
    """
    Login service to get a JWT token.

    Args:
        token (str): JWT token.

    Returns:
        dict: Login response.
    """

    url = f"{config.CIVA_API_URL}/Account/login"
    body = {"token": token}
    response = requests.post(url, json=body)
    response.raise_for_status()

    return response.json()
