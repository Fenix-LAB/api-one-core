import requests
import json
from config.config import config
from app.schemas.generic_list import ListResponse
from app.schemas.requirements.response import (
    SectionOptionRequerimientosResponse,
    RequerimientoElementResponse,
    RequerimientosEvidenciaResponse,
    SolicitudesSectionRequerimientosOptionResponse,
    SolicitudResponse,
)

async def fetch_section_list(date_ini: str, date_end: str, token: str):
    pass

async def fetch_requerimientos_list(code: int, date_ini: str, date_end: str, token: str):
    pass

async def fetch_evidencia_id(id: str, code_section: int, token: str):
    pass

async def fetch_halazagos_list(code_section: int, token: str):
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
