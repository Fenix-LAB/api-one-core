import requests
from config.config import config


async def fetch_requirement_obligation(date_ini: str, date_end: str, token: str) -> tuple:
    """
    Method to fetch requirement obligations.

    Args:
        date_ini (str): Initial date.
        date_end (str): End date.

    Returns:
        tuple: Requirement obligations.
    """

    url = f"{config.CIVA_API_URL}/Dashboard/getRequerimientoObligaciones"
    body = {
        "dateIni": date_ini.isoformat(),  # '2025-03-01T12:00:00'
        "dateEnd": date_end.isoformat()   # '2025-03-05T18:30:00'
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()

    data = response.json()

    return data["data"], data["token"]