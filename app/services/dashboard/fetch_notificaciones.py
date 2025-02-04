import requests
from config.config import config


async def fetch_notificaciones(page_size: int, current_page: int, token: str) -> tuple:
    """
    Method to fetch all notifications.

    Args:
        token (str): Token.

    Returns:

    """

    url = f"{config.CIVA_API_URL}/Dashboard/getNotificaciones"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "pageSize": page_size,
        "currentPage": current_page
    }
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()

    data = response.json()

    return data["data"], data["token"]
