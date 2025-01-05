from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.requirements.response import RequerementsObligationsResponse

from app.services.get_requirement_obligation import get_requerimiento_obligaciones
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger


app = APIRouter()
security = HTTPBearer()

@app.post("requirements/get_section_list")
@inject
async def getSectionList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_section_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )


@app.post("requirements/get_requerimientos_list")
@inject
async def getRequerimientosList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_requerments_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("requirements/get_evidence_id")
@inject
async def getEvidenciaID(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_evience_id: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/get_finding_list")
@inject
async def getHallazgosList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_finding_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/save_evidence")
@inject
async def saveEvidencia(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save ecidence.

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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/save_evidence: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/save_finding")
@inject
async def saveHallazgo(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/save_finding: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/get_section_request_list")
@inject
async def getSolicitudesSectionList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save a finding.

    ## REQUEST
    - DateIni
    - DateEnd

    ## RESPONSE
    - Code
    - Cantidad
    - Total
    - CantidadSolicitudes

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_section_request_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/get_request_list")
@inject
async def getSolicitudesList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_request_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/get_request_by_id")
@inject
async def getSolicitudID(
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_request_by_id: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/=save_request")
@inject
async def saveSolicitud(
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

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/gsave_request: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("requirements/get_request_by_id")
@inject
async def getSolicitudID(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a request by id.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - 200: Success
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 500: Internal Server Error

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /requirements/get_request_by_id: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )