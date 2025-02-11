from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse

from app.schemas.requirements.response import (
    SectionOptionRequerimientosResponse,
    RequerimientoElementResponse,
    RequerimientosEvidenciaResponse,
    SolicitudesSectionRequerimientosOptionResponse,
    SolicitudResponse,
)

from app.schemas.requirements.request import (
    SectionRequerimientosListRequest,
    RequerimientosListRequest,
    RequerimientosEvidenciaIDRequest,
    RequerimientosHallazgosListRequest,
    RequerimientosEvidenciaSaveRequest,
    HallazgoSaveRequest,
    SolicitudIDRequest,
    SolicitudSaveRequest,
)

from app.services.requirement.requirement_services import *

from app.schemas.models.area_rol import AreaRolModel
from app.schemas.models.responsable import ResponsableModel
from app.schemas.models.file_info import FileInfoModel  
from app.schemas.models.hallazgo_option import HallazgoOptionModel

from app.services.get_requirement_obligation import get_requerimiento_obligaciones
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()


@app.post("/getSectionList")
@inject
async def getSectionList(
    request: SectionRequerimientosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of sections.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Code
    - Cantidad
    - Total
    - ProximosVencer
    - Selected
    - Enable

    """

    logger.info(f"ENDPOINT /getSectionList: {request}")

    try:

        data, token = await fetch_section_list(
            date_ini=request.dateIni,
            date_end=request.dateEnd,
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSectionList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getRequerimientosList")
@inject
async def getRequerimientosList(
    request: RequerimientosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of requirements.

    ## REQUEST
    - Code
    - DateIni
    - DateEnd

    ## RESPONSE
    - ID
    - Verificacion
    - Usuario
    - Elementos
    - Vencimiento
    - FechaEnvio
    - EsCritico

    """

    logger.info(f"ENDPOINT /getRequerimientosList: {request}")

    try:

        data, token = await fetch_requerimientos_list(
            code=request.code,
            date_ini=request.dateIni,
            date_end=request.dateEnd,
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getRequerimientosList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getEvidenciaID")
@inject
async def getEvidenciaID(
    request: RequerimientosEvidenciaIDRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a evidence id.

    ## REQUEST
    - ID
    - CodeSection

    ## RESPONSE
    - ID
    - Elemento
    - CaseNumber
    - Status
    - FechaInicio
    - FechaVencimiento
    - ProximoVencer
    - AreaRols
    - Responsables
    - Archivos
    - Ubicacion
    - Comentarios
    - HallazgoComentarios
    - HallazgoRecomendaciones

    """

    logger.info(f"ENDPOINT /getEvidenciaID: {request}")

    try:

        evidencia, token = await fetch_evidencia_id(
            id=request.id,
            code_section=request.codeSection,
            token=user_data.token,
        )

        if evidencia is None:
            return ApiResponse(
                success=False,
                message="No data found",
                data=None,
                token=None,
            )

        return ApiResponse(
            success=True,
            message="OK",
            data=evidencia,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getEvidenciaID: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getHallazgosList")
@inject
async def getHallazgosList(
    request: RequerimientosHallazgosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of findings.

    ## REQUEST
    - CodeSection

    ## RESPONSE
    - ID
    - Code
    - Nombre

    """

    logger.info(f"ENDPOINT /getHallazgosList: {request}")

    try:

        data, token = await fetch_hallazgos_list(
            code_section=request.codeSection,
            token=user_data.token,
        )

        if data is None:
            return ApiResponse(
                success=False,
                message="No data found",
                data=None,
                token=None,
            )
        
        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getHallazgosList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveEvidencia")
@inject
async def saveEvidencia(
    request: RequerimientosEvidenciaSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    Me dio error
    ## DESCRIPTION
    ### Endpoint to save evidence.

    ## REQUEST
    - ID
    - AreaRols
    - Responsables
    - Archivos
    - Ubicacion
    - Comentarios

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    logger.info(f"ENDPOINT /saveEvidencia: {request}")

    try:

        response = await save_evidencia(
            data=request,
            token=user_data.token,
        )

        if response.status_code != 200:
            return ApiResponse(
                success=False,
                message="Bad Request",
                data=False,
                token=None,
            )

        return ApiResponse(
            success=True,
            message="OK",
            data=True,
            token=None,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /saveEvidencia: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=False,
            token=None,
        )


@app.post("/saveHallazgo")
@inject
async def saveHallazgo(
    request: HallazgoSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    Me dio error
    ## DESCRIPTION
    ### Endpoint to save a finding.

    ## REQUEST
    - ID
    - CodeSection
    - EsHallazgo
    - Comentarios
    - HallazgoCode
    - HallazgoComentarios
    - Recomendaciones

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    logger.info(f"ENDPOINT /saveHallazgo: {request}")

    try:

        response = await save_hallazgo(
            data=request,
            token=user_data.token,
        )

        if response.status_code != 200:
            return ApiResponse(
                success=False,
                message="Bad Request",
                data=False,
                token=user_data.token,
            )
        
        return ApiResponse(
            success=True,
            message="OK",
            data=True,
            token=None,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /saveHallazgo: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=False,
            token=None,
        )


@app.post("/getSolicitudesSectionList")
@inject
async def getSolicitudesSectionList(
    request: SectionRequerimientosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of solicitude sections.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Code
    - Cantidad
    - Total
    - CantidadSolicitudes

    """

    logger.info(f"ENDPOINT /getSolicitudesSectionList: {request}")

    try:

        data, token = await fetch_solicitudes_section_list(
            date_ini=request.dateIni,
            date_end=request.dateEnd,
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSolicitudesSectionList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getSolicitudesList")
@inject
async def getSolicitudesList(
    request: RequerimientosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    Me dio error (schema no coincide)
    ## DESCRIPTION
    ### Endpoint to get a list of requests.

    ## REQUEST
    - Code
    - DateIni
    - DateEnd

    ## RESPONSE
    - ID
    - Verificacion
    - Usuario
    - Elementos
    - Vencimiento
    - FechaEnvio
    - EsCritico

    """

    logger.info(f"ENDPOINT /getSolicitudesList: {request}")

    try:
        # data = [
        #     RequerimientoElementResponse(ID=1, Verificacion="NuevaSolicitud", Usuario="Vombergar", Elementos="Capturas de pantalla del RFC activo", Vencimiento="30 días"),
        #     RequerimientoElementResponse(ID=2, Verificacion="NuevaSolicitud", Usuario="Iker Muniain", Elementos="Manifestar si existió alta, baja...", Vencimiento="8 días"),
        #     RequerimientoElementResponse(ID=3, Verificacion="NuevaSolicitud", Usuario="Romagnoli", Elementos="Manifestar si existió alta, baja...", Vencimiento="30 días"),
        #     RequerimientoElementResponse(ID=4, Verificacion="NuevaSolicitud", Usuario="Romaña", Elementos="Reporte de importaciones...", Vencimiento="80 días"),
        # ]

        data, token = await fetch_solicitud_list(
            code=request.code,
            date_ini=request.dateIni,
            date_end=request.dateEnd,
            token=user_data.token,
        )
        return ApiResponse(
            success=True,
            message="OK",
            data=ListResponse(data=data),
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSolicitudesList: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getSolicitudID")
@inject
async def getSolicitudID(
    request: SolicitudIDRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a request by id.

    ## REQUEST
    - ID
    - CodeSection

    ## RESPONSE
    - ID
    - Elemento
    - CaseNumber
    - Cliente
    - Status
    - FechaRevision
    - AreaRols
    - Responsables

    """

    logger.info(f"ENDPOINT /getSolicitudID: {request}")

    try:
        solicitud = SolicitudResponse(
            ID=1,
            Elemento="Elemento 1 Captura de pantalla de Informes de descargos obtenidos del portal de Anexo 30 (SCCCYG) (última modificación en su caso)",
            CaseNumber=123,
            Cliente="Cliente 1",
            Status="RevisionPendiente",
            FechaRevision="2024-01-01T00:00:00",
            AreaRols=[
                AreaRolModel(Code="Comex"),
                AreaRolModel(Code="Legal"),
            ],
            Responsables=[
                ResponsableModel(ID=1, Nombre="Walter Mazzantti", AreaCode="Fiscal"),
                ResponsableModel(ID=2, Nombre="Iker Muniain", AreaCode="Finanzas"),
            ],
        )

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=solicitud,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSolicitudID: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/saveSolicitud")
@inject
async def saveSolicitud(
    request: SolicitudSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save a request.

    ## REQUEST
    - ID
    - IsAprobado
    - AreaRols
    - Responsables

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    logger.info(f"ENDPOINT /saveSolicitud: {request}")

    try:
        # Simulate a successful operation
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=True,
            Token=user_data.token,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /saveSolicitud: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getSolicitudID")
@inject
async def getSolicitudID(
    request: SolicitudIDRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a request by id.

    ## REQUEST
    - ID
    - CodeSection

    ## RESPONSE
    - ID
    - Elemento
    - CaseNumber
    - Cliente
    - Status
    - FechaRevision
    - AreaRols
    - Responsables

    """

    logger.info(f"ENDPOINT /getSolicitudID: {request}")

    try:
        solicitud = SolicitudResponse(
            ID=1,
            Elemento="Elemento 1 Captura de pantalla de Informes de descargos obtenidos del portal de Anexo 30 (SCCCYG) (última modificación en su caso)",
            CaseNumber=1,
            Status="RevisionPendiente",
            FechaRevision="2024-01-01",
            Cliente="Cliente 1",
            AreaRols=[
                AreaRolModel(Code="Comex"),
                AreaRolModel(Code="Legal")
            ],
            Responsables=[
                ResponsableModel(ID=1, Nombre="Walter Mazzantti", AreaCode="Fiscal"),
                ResponsableModel(ID=2, Nombre="Iker Muniain", AreaCode="Finanzas")
            ]
        )

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=solicitud,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSolicitudID: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )
