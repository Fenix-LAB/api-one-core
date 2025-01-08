from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic.date_request import DateRequest

from app.schemas.generic_response import ApiResponse
from app.schemas.dashboard import (
    ExpedienteCivaResponse,
    RequirementObligationsResponse,
)

from app.services.get_requirement_obligation import get_requerimiento_obligaciones
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()


@app.post("/GetRequirementObligation")
@inject
async def GetRequirementObligation(
    request: DateRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of requirements obligations.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Pendientes
    - Proximos
    - Hallazgos

    """

    try:

        pending, near_due, findings = await get_requerimiento_obligaciones(db_session)

        response = RequirementObligationsResponse(
            Pending=pending, NearDue=near_due, Findings=findings
        )

        return ApiResponse(
            Status="200",
            Message="Fetched requirements obligations successfully",
            Data=response,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /GetRequirementObligation: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )


@app.post("/getGetExpedienteCiva")
@inject
async def getGetExpedienteCiva(
    request: DateRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of expediente civa.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Actualizacion (datetime)

    """

    try:

        return ApiResponse(
            Status="200", Message="Not Implemented", Data=None, Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getGetExpedienteCiva: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )


@app.post("/getTotalSolicitudesRevisor")
@inject
async def getTotalSolicitudesRevisor(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of expediente civa.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Solicitudes

    """

    try:

        return ApiResponse(
            Status="200", Message="Not Implemented", Data=None, Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /GetRequirementObligation: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )


@app.post("/getNotificaciones")
@inject
async def getNotificaciones(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of expediente civa.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - Titulo
    - Referencia
    - Estado
    - Descripcion
    - Fecha
    - EsError

    """

    try:

        return ApiResponse(
            Status="200", Message="Not Implemented", Data=None, Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /dashboard/get_notifications: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )


@app.post("/getDonutPanel")
@inject
async def getDonutPanel(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of expediente civa.

    ## REQUEST
    - DateIni
    - DateEnd
    - Type
        - Expediente
        - Requerimiento
        - Verificacion
        - TareasPendientes

    ## RESPONSE
    - ColorCode
        - Green
        - Red
        - Orange
    - NombreCode
        - Completado
        - Pendiente
        - Hallazgos
        - Bajo
        - Medio
        - Alto
    - Porcentaje
    - Cantidad

    """

    try:

        return ApiResponse(
            Status="200", Message="Not Implemented", Data=None, Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getDonutPanel: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )


@app.post("/getTareasResponsable")
@inject
async def getTareasResponsable(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of expediente civa.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Area
    - Usuario
    - Asignadas
    - Completadas
    - RiesgoCode
        - Alto
        - Medio
        - Bajo

    """

    try:

        return ApiResponse(
            Status="200", Message="Not Implemented", Data=None, Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getTareasResponsable: {e}")
        return ApiResponse(
            Status="500", Message="Internal Server Error", Data=None, Token=user_data.token
        )
