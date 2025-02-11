import requests
import json
from config.config import config
from config.logger_config import logger
from app.schemas.generic_list import ListResponse
from app.schemas.models.responsable import ResponsableModel


async def fetch_responsables(token: str) -> tuple:
    """
    Fetch responsables
    Args:
        token (str): Token
    Returns:
        list: List of responsables
    """
    url = f"{config.CIVA_API_URL}/Comunes/getResponsables"
    headers = {"Authorization": f"Bearer {token}"}
    body = {}
    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None
    
    responsables = ListResponse[ResponsableModel](**response_data["data"])

    return responsables, response_data["token"]