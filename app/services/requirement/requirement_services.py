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
    
    print("====================================================")
    
    print(response_data)

    response = RequerimientosEvidenciaResponse(**response_data["data"])

    return response, response_data["token"]

async def fetch_hallazgos_list(code_section: int, token: str):
    pass

async def save_evidencia(data: dict, token: str):
    pass

async def save_hallazgo(data: dict, token: str):
    pass

async def fetch_solicitudes_section_list(date_ini: str, date_end: str, token: str):
    pass

async def fetch_solicitud_list(code: int, date_ini: str, date_end: str, token: str):
    pass

async def fetch_solicitud_id(id: str, code_section: int, token: str):
    pass

async def save_solicitud(data: dict, token: str):
    pass
