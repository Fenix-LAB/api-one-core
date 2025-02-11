import requests
import json
from config.config import config
from config.logger_config import logger
from app.schemas.generic_list import ListResponse
from app.schemas.requirements.response import (
    SectionOptionRequerimientosResponse,
    RequerimientoElementResponse,
    RequerimientosEvidenciaResponse,
    SolicitudesSectionRequerimientosOptionResponse,
    SolicitudResponse,
)
from app.schemas.models.hallazgo_option import HallazgoOptionModel

async def fetch_section_list(date_ini: str, date_end: str, token: str) -> tuple:
    """
    Fetch section list

    Args:
        date_ini (str): Date ini
        date_end (str): Date end
        token (str): Token
    
    Returns:
        tuple: (ListResponse, token)
    
    """

    url = f"{config.CIVA_API_URL}/Requerimientos/getSectionList"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "date_ini": date_ini.isoformat(), 
        "date_end": date_end.isoformat()
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    list_response = ListResponse[SectionOptionRequerimientosResponse](**response_data["data"])

    return list_response, response_data["token"]

async def fetch_requerimientos_list(code: int, date_ini: str, date_end: str, token: str):
    """
    Fetch requerimientos list
    
    Args:
        code (int): Code
        date_ini (str): Date ini
        date_end (str): Date end
        token (str): Token
        
    Returns:
        tuple: (ListResponse, token)

        """
    
    url = f"{config.CIVA_API_URL}/Requerimientos/getRequerimientosList"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "code": code.value,
        "dateIni": date_ini.isoformat(),
        "dateEnd": date_end.isoformat()
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    list_response = ListResponse[RequerimientoElementResponse](**response_data["data"])

    return list_response, response_data["token"]

async def fetch_evidencia_id(id: str, code_section: int, token: str):
    """
    Fetch evidencia id
    
    Args:
        id (str): Id
        code_section (int): Code section
        token (str): Token
        
    Returns:
        tuple: (RequerimientosEvidenciaResponse, token)

        """
    
    url = f"{config.CIVA_API_URL}/Requerimientos/getEvidenciaId"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "id": str(id),
        "code_section": code_section.value
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    response = RequerimientosEvidenciaResponse(**response_data["data"])

    return response, response_data["token"]

async def fetch_hallazgos_list(code_section: int, token: str):
    """
    Fetch hallazgos list
    
    Args:
        code_section (int): Code section
        token (str): Token
        
    Returns:
        tuple: (ListResponse, token)

        """
    
    url = f"{config.CIVA_API_URL}/Requerimientos/getHallazgosList"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "code_section": code_section.value
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    list_response = ListResponse[HallazgoOptionModel](**response_data["data"])

    return list_response, response_data["token"]

async def save_evidencia(data, token: str):
    """
    Save evidencia
    
    Args:
        data (dict): Data
        token (str): Token

    Returns:
        tuple: (bool, token)

    """

    request_dict = data.model_dump(mode="json")

    url = f"{config.CIVA_API_URL}/Requerimientos/saveEvidencia"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers, json=request_dict)
    response_data = response.raise_for_status()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    return response_data


async def save_hallazgo(data: dict, token: str):
    """
    Save hallazgo
    
    Args:
        data (dict): Data
        token (str): Token

    Returns:
        tuple: (bool, token)

    """

    request_dict = data.model_dump(mode="json")

    url = f"{config.CIVA_API_URL}/Requerimientos/saveHallazgo"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers, json=request_dict)
    response_data = response.raise_for_status()

    print("====================================")
    print(response_data)
    print("====================================")

    return response_data

async def fetch_solicitudes_section_list(date_ini: str, date_end: str, token: str):
    """
    
    Fetches the list of solicitude sections between the given dates.

    Args:
        date_ini (str): Start date.
        date_end (str): End date.
        token (str): Authentication token.

    Returns:
        ListResponse: List of solicitude sections
    """

    url = f"{config.CIVA_API_URL}/Requerimientos/getSolicitudesSectionList"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "date_ini": date_ini.isoformat(),
        "date_end": date_end.isoformat()
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    list_response = ListResponse[SolicitudesSectionRequerimientosOptionResponse](**response_data["data"])

    return list_response, response_data["token"]

async def fetch_solicitud_list(code: int, date_ini: str, date_end: str, token: str):
    """
    Fetches the list of solicitudes between the given dates.

    Args:
        code (int): Section code.
        date_ini (str): Start date.
        date_end (str): End date.
        token (str): Authentication token.

    Returns:
        ListResponse: List of solicitudes.
    """

    url = f"{config.CIVA_API_URL}/Requerimientos/getSolicitudesList"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "code": code,
        "dateIni": date_ini.isoformat(),
        "dateEnd": date_end.isoformat()
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data.get("success") == False:
        logger.error("Invalid response data structure")
        return None, None

    # list_response = ListResponse[RequerimientoElementResponse](**response_data["data"])

    return list_response, response_data["token"]

async def fetch_solicitud_id(id: str, code_section: int, token: str):
    """
    Fetches the solicitude with the given id.

    Args:
        id (str): Solicitude id.
        code_section (int): Section code.
        token (str): Authentication token.

    Returns:
        SolicitudResponse: Solicitude data.
    """

    url = f"{config.CIVA_API_URL}/Requerimientos/getSolicitudId"
    headers = {"Authorization": f"Bearer {token}"}
    body = {
        "id": str(id),
        "code_section": code_section.value
    }

    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    if response_data["data"] is None:
        return None, None

    response = SolicitudResponse(**response_data["data"])

    return response, response_data["token"]

async def save_solicitud(data: dict, token: str):
    """
    Saves the solicitude data.

    Args:
        data (dict): Solicitude data.
        token (str): Authentication token.

    Returns:
        bool: True if the data was saved successfully.
    """

    request_dict = data.model_dump(mode="json")

    url = f"{config.CIVA_API_URL}/Requerimientos/saveSolicitud"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers, json=request_dict)
    response_data = response.raise_for_status()

    return response_data
