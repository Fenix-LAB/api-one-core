from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic.date_request import DateRequest

from app.schemas.generic_response import ApiResponse

from app.schemas.dashboard.request import (
    RequerimientoObligacionesRequest,
    ExpedienteCivaRequest,
    TotalSolicitudesRevisorRequest,
    NotificacionesRequest,
    DonutPanelRequest,
    TareaResponsableRequest,
)

from app.schemas.dashboard.response import (
    ExpedienteCivaResponse,
    RequerimientoObligacionesResponse,
    NotificationResponse,
    DonutPanelResponse,
    TareaResponsableResponse,
    TotalSolicitudesRevisorResponse,
)


from app.services.dashboard import (
    fetch_requirement_obligation,
    fetch_expediente_civa,
    fetch_total_solicitudes_revisor,
    fetch_notificaciones,
    fetch_donut_panel,
    fetch_tareas_responsable,
)
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()


@app.post("/GetRequirementObligation")
@inject
async def GetRequirementObligation(
    request: RequerimientoObligacionesRequest,
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

    logger.info(f"ENDPOINT /GetRequirementObligation: {request}")

    try:

        # response = RequerimientoObligacionesResponse(
        #     Pendientes=10, Proximos=5, Hallazgos=3
        # )

        logger.info(f"Fetching requirement obligations ...")

        response = await fetch_requirement_obligation(
            bq_client=db_session, date_ini=request.DateIni, date_end=request.DateEnd
        )

        logger.info(f"Requirement obligations fetched successfully")

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
    request: ExpedienteCivaRequest,
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

    logger.info(f"ENDPOINT /getGetExpedienteCiva: {request}")

    try:

        # response = ExpedienteCivaResponse(Actualizacion="2023-12-01T12:00:00")

        logger.info(f"Fetching expediente civa ...")

        response = await fetch_expediente_civa(
            bq_client=db_session, date_ini=request.DateIni, date_end=request.DateEnd
        )

        logger.info(f"Expediente civa fetched successfully")

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
    request: TotalSolicitudesRevisorRequest,
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

    logger.info(f"ENDPOINT /getTotalSolicitudesRevisor: {request}")

    try:

        # response = TotalSolicitudesRevisorResponse(Solicitudes=9998)

        logger.info(f"Fetching total solicitudes revisor ...")

        response = await fetch_total_solicitudes_revisor(
            bq_client=db_session, date_ini=request.DateIni, date_end=request.DateEnd
        )

        logger.info(f"Total solicitudes revisor fetched successfully")

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
    request: NotificacionesRequest,
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

    logger.info(f"ENDPOINT /getNotificaciones: {request}")

    try:

        # data = [
        #     NotificationResponse(
        #         Titulo="Subject",
        #         Referencia="0000000001",
        #         Estado="Hallazgo",
        #         Descripcion="Cum sociis natoque penatibus et magnis dis parturient montes, nascetur lorem ...",
        #         Fecha="2023-12-01T11:00:00",
        #         EsError=True,
        #     ),
        #     NotificationResponse(
        #         Titulo="Subject",
        #         Referencia="0000000002",
        #         Estado="Solicitud Aprobada",
        #         Descripcion="Cum sociis natoque penatibus et magnis dis parturient montes, nascetur lorem ...",
        #         Fecha="2023-12-01T10:00:00",
        #         EsError=False,
        #     ),
        # ]

        logger.info(f"Fetching notifications ...")

        data = await fetch_notificaciones(bq_client=db_session)

        logger.info(f"Notifications fetched successfully")

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
    request: DonutPanelRequest,
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

    logger.info(f"ENDPOINT /getDonutPanel: {request}")

    try:

        # data = [
        #     DonutPanelResponse(
        #         NombreCode="Completado",
        #         Porcentaje=5,
        #         Cantidad=45,
        #         ColorCode="Green",
        #     ),
        #     DonutPanelResponse(
        #         NombreCode="Pendiente",
        #         Porcentaje=95,
        #         Cantidad=920,
        #         ColorCode="Red",
        #     ),
        # ]

        logger.info(f"Fetching donut panel ...")

        data = await fetch_donut_panel(
            bq_client=db_session, date_ini=request.DateIni, date_end=request.DateEnd, panel_type=request.Type
        )

        logger.info(f"Donut panel fetched successfully")

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
    request: TareaResponsableRequest,
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

    logger.info(f"ENDPOINT /getTareasResponsable: {request}")

    try:

        # data = [
        #     TareaResponsableResponse(
        #         Area="Rrhh",
        #         Usuario="Nombre Usuario",
        #         Asignadas=10,
        #         Completadas=10,
        #         RiesgoCode="Medio",
        #     ),
        #     TareaResponsableResponse(
        #         Area="Finanzas",
        #         Usuario="Nombre Usuario",
        #         Asignadas=10,
        #         Completadas=10,
        #         RiesgoCode="Alto",
        #     ),
        # ]

        logger.info(f"Fetching tareas responsables ...")

        data = await fetch_tareas_responsable(
            bq_client=db_session, date_ini=request.DateIni, date_end=request.DateEnd
        )

        logger.info(f"Tareas responsables fetched successfully")

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
