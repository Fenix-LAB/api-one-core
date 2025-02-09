import requests
import json
from config.config import config
from app.schemas.company_data.response import (
    SectionOptionDatosEmpresaResponse,
    HistoricoResponse,
    RazonSocialResponse,
    DatosEmpresaEvidenciaResponse,
    ClienteProveedorResponse,
    ProveedorNacionalResponse,
    SocioAccionistaResponse,
    LegalUsoResponse,
    EnlaceOperativoResponse,
)
from app.schemas.generic_list import ListResponse

async def fetch_section_list(date_ini: str, date_end: str, token: str) -> tuple:
    """
    Method to fetch section list.

    Args:
        date_ini (str): Initial date.
        date_end (str): End date.

    Returns:
        tuple: Section list.
    """

    url = f"{config.CIVA_API_URL}/DatosEmpresa/getSectionList"
    body = {
        "dateIni": date_ini.isoformat(),  # '2025-03-01T12:00:00'
        "dateEnd": date_end.isoformat()   # '2025-03-05T18:30:00'
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()

    res = response.json()

    list_response = ListResponse[SectionOptionDatosEmpresaResponse](
        **res["data"]
    )

    return list_response , res["token"]

async def fetch_razon_social_historico_list(token: str) -> tuple:
    """
    Method to fetch razon social historico list.

    Args:
        code_section (str): Section code.
        date_ini (str): Initial date.
        date_end (str): End date.

    Returns:
        tuple: Razon social historico list.
    """

    url = f"{config.CIVA_API_URL}/DatosEmpresa/getRazonSocialHistoricoList"
    body = {}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()

    res = response.json()

    list_response = ListResponse[HistoricoResponse](
        **res["data"]
    )

    return list_response , res["token"]

async def save_razon_social(request: dict, token: str) -> tuple:
    """
    Method to fetch razon social.
SS
    Args:
        code_section (str): Section code.

    Returns:
        tuple: Razon social.
    """

    request_dict = request.model_dump()
    request_dict = json.loads(json.dumps(request_dict, default=str))

    url = f"{config.CIVA_API_URL}/DatosEmpresa/saveRazonSocial"
    headers = {"Authorization": f"Bearer {token}"}
    print(f'REQUEST: {request_dict}')

    try:
        response = requests.post(url, json=request_dict, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            return True

    except Exception as e:
        return False

async def fetch_hallazgos_list(code_section: str, token: str) -> tuple:
    """
    Method to fetch hallazgos list.

    Args:
        code_section (str): Section code.

    Returns:
        tuple: Hallazgos list.
    """

    pass

async def fetch_evidencia_id(id: str, code_section: str, token: str) -> tuple:
    """
    Method to fetch evidencia id.

    Args:
        id (str): Evidencia id.
        code_section (str): Section code.

    Returns:
        tuple: Evidencia id.
    """

    pass

async def save_evidencia(data: dict, token: str) -> tuple:
    """
    Method to save evidencia.

    Args:
        data (dict): Evidencia data.

    Returns:
        tuple: Evidencia data.
    """

    pass

async def fetch_paises(token: str) -> tuple:
    """
    Method to fetch paises.

    Returns:
        tuple: Paises.
    """

    pass

async def fetch_paises_estados(iid_pais: str, token: str) -> tuple:
    """
    Method to fetch paises estados.

    Args:
        iid_pais (str): Pais id.

    Returns:
        tuple: Paises estados.
    """

    pass

async def get_cliente_proveedor_list(token: str) -> tuple:
    """
    Method to get cliente proveedor list.

    Returns:
        tuple: Cliente proveedor list.
    """

    pass

async def save_cliente_proveedor(data: dict, token: str) -> tuple:
    """
    Method to save cliente proveedor.

    Args:
        data (dict): Cliente proveedor data.

    Returns:
        tuple: Cliente proveedor data.
    """

    pass

async def fetch_provedor_nacional_list(token: str) -> tuple:
    """
    Method to fetch provedor nacional list.

    Returns:
        tuple: Provedor nacional list.
    """

    pass

async def save_provedor_nacional(data: dict, token: str) -> tuple:
    """
    Method to save provedor nacional.

    Args:
        data (dict): Provedor nacional data.

    Returns:
        tuple: Provedor nacional data.
    """

    pass

async def fetch_caracter_tipos(token: str) -> tuple:
    """
    Method to get caracter tipos.

    Returns:
        tuple: Caracter tipos.
    """

    pass

async def fetch_socio_accionista_list(token: str) -> tuple:
    """
    Method to fetch socio accionista list.

    Returns:
        tuple: Socio accionista list.
    """

    pass

async def save_socio_accionista(data: dict, token: str) -> tuple:
    """
    Method to save socio accionista.

    Args:
        data (dict): Socio accionista data.

    Returns:
        tuple: Socio accionista data.
    """

    pass


async def save_legal_uso(data: dict, token: str) -> tuple:
    """
    Method to save legal uso.

    Args:
        data (dict): Legal uso data.

    Returns:
        tuple: Legal uso data.
    """

    pass

async def fetch_enlaces_operativos_list(token: str) -> tuple:
    """
    Method to fetch enlaces operativos list.

    Returns:
        tuple: Enlaces operativos list.
    """

    pass


async def save_enlaces_operativos(data: dict, token: str) -> tuple:
    """
    Method to save enlaces operativos.

    Args:
        data (dict): Enlaces operativos data.

    Returns:
        tuple: Enlaces operativos data.
    """

    pass

async def fetch_domicilio_list(token: str) -> tuple:
    """
    Method to fetch domicilio list.

    Returns:
        tuple: Domicilio list.
    """

    pass

async def save_domicilio(data: dict, token: str) -> tuple:
    """
    Method to save domicilio.

    Args:
        data (dict): Domicilio data.

    Returns:
        tuple: Domicilio data.
    """

    pass

