import requests
from config.config import config

async def fetch_section_list(date_ini: str, date_end: str, token: str) -> tuple:
    """
    Method to fetch section list.

    Args:
        date_ini (str): Initial date.
        date_end (str): End date.

    Returns:
        tuple: Section list.
    """

    url = f"{config.CIVA_API_URL}/Dashboard/getSecciones"
    body = {
        "dateIni": date_ini.isoformat(),  # '2025-03-01T12:00:00'
        "dateEnd": date_end.isoformat()   # '2025-03-05T18:30:00'
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()

    data = response.json()

    return data["data"], data["token"]

async def fetch_razon_social_historico_list(code_section: str, token: str) -> tuple:
    """
    Method to fetch razon social historico list.

    Args:
        code_section (str): Section code.
        date_ini (str): Initial date.
        date_end (str): End date.

    Returns:
        tuple: Razon social historico list.
    """

    pass

async def fetch_razon_social(code_section: str, token: str) -> tuple:
    """
    Method to fetch razon social.

    Args:
        code_section (str): Section code.

    Returns:
        tuple: Razon social.
    """

    pass

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

