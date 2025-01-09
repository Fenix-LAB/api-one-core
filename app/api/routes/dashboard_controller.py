from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic.date_request import DateRequest

from app.schemas.generic_response import ApiResponse
from app.schemas.dashboard.response import (
    ExpedienteCivaResponse,
    RequirementObligationsResponse,
    NotificationResponse,
    DonutPanelResponse,
    TareaResponsableResponse,
    TotalSolicitudesRevisorResponse,
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

        response = RequirementObligationsResponse(
            Pendientes=10, Proximos=5, Hallazgos=3
        )

        return ApiResponse(
            Success=True,
            Message="Fetched requirements obligations successfully",
            Data=response,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /GetRequirementObligation: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
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
    ### Endpoint to get expediente civa details.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Actualizacion (datetime)

    """

    try:

        response = ExpedienteCivaResponse(Actualizacion="2023-12-01T12:00:00")

        return ApiResponse(
            Success=True,
            Message="Fetched expediente civa successfully",
            Data=response,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getGetExpedienteCiva: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
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
    ### Endpoint to get total solicitudes revisor.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Solicitudes

    """

    try:

        response = TotalSolicitudesRevisorResponse(Solicitudes=9998)

        return ApiResponse(
            Success=True,
            Message="Fetched total solicitudes successfully",
            Data=response,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getTotalSolicitudesRevisor: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
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
    ### Endpoint to get notifications.

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

        data = [
            NotificationResponse(
                Titulo="Subject",
                Referencia="0000000001",
                Estado="Hallazgo",
                Descripcion="Cum sociis natoque penatibus et magnis dis parturient montes, nascetur lorem ...",
                Fecha="2023-12-01T11:00:00",
                EsError=True,
            ),
            NotificationResponse(
                Titulo="Subject",
                Referencia="0000000002",
                Estado="Solicitud Aprobada",
                Descripcion="Cum sociis natoque penatibus et magnis dis parturient montes, nascetur lorem ...",
                Fecha="2023-12-01T10:00:00",
                EsError=False,
            ),
        ]

        return ApiResponse(
            Success=True,
            Message="Fetched notifications successfully",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getNotificaciones: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
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
    ### Endpoint to get donut panel data.

    ## REQUEST
    - DateIni
    - DateEnd
    - Type

    ## RESPONSE
    - ColorCode
    - NombreCode
    - Porcentaje
    - Cantidad

    """

    try:

        data = [
            DonutPanelResponse(
                NombreCode="Completado",
                Porcentaje=5,
                Cantidad=45,
                ColorCode="Green",
            ),
            DonutPanelResponse(
                NombreCode="Pendiente",
                Porcentaje=95,
                Cantidad=920,
                ColorCode="Red",
            ),
        ]

        return ApiResponse(
            Success=True,
            Message="Fetched donut panel successfully",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getDonutPanel: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
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
    ### Endpoint to get tareas responsables data.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Area
    - Usuario
    - Asignadas
    - Completadas
    - RiesgoCode

    """

    try:

        data = [
            TareaResponsableResponse(
                Area="Rrhh",
                Usuario="Nombre Usuario",
                Asignadas=10,
                Completadas=10,
                RiesgoCode="Medio",
            ),
            TareaResponsableResponse(
                Area="Finanzas",
                Usuario="Nombre Usuario",
                Asignadas=10,
                Completadas=10,
                RiesgoCode="Alto",
            ),
        ]

        return ApiResponse(
            Success=True,
            Message="Fetched tareas responsables successfully",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getTareasResponsable: {e}")
        return ApiResponse(
            Success=False, Message="Internal Server Error", Data=None, Token=user_data.token
        )
