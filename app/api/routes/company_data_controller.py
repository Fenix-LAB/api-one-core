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

@app.post("/company_data/get_section_list")
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
    - Selected

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_section_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )

@app.post("/company_data/get_social_reason_list")
@inject
async def getRazonSocialHistoricoList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get social reason history list.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber
    - IsCompany
    - Name
    - RFC
    - Folio
    - MovementDate
    - DeedDate
    - Fedatario
    - Notary
    - Effect
        - RazonSocial
        - Fusion
        - Escision
        - CambioObjeto
        - Estatutos
    - Notice
    - NoticeDate

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_section_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_social_reason")
@inject
async def saveRazonSocial(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save social reason.

    ## REQUEST
    - ID
    - CaseNumber
    - IsCompany
    - Name
    - RFC
    - Folio
    - MovementDate
    - DeedDate
    - Fedatario
    - Notary
    - Effect
    - Notice
    - NoticeDate

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
        logger.error(f"ENDPOINT /company_data/save_social_reason: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )


@app.post("/company_data/get_findings_list")
@inject
async def getHallazgosList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get findings list.

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
        logger.error(f"ENDPOINT /company_data/get_findings_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/get_evidence_by_id")
@inject
async def getEvidenciaID(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get findings list.

    ## REQUEST
    - ID
    - CodeSection

    ## RESPONSE
    - ID
    - CaseNumber
    - Fecha
    - AreaRole
        - Code
            - Administrador
            - Rrhh
            - Finanzas
            - Fiscal
            - Comex
            - Legal
            - Revisor
        - Name
    - Responsables
        - ID
        - Nombre
        - AreaCode
    - Recomendaciones
    - Cliente
    - Hallazgo
        - ID
        - Code
        - Nombre
    - HallazgoComentarios

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_evidence_by_id: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_evidence")
@inject
async def saveEvidencia(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save evidence.

    ## REQUEST
    - ID
    - CodeSection
    - IsHallazgo
    - AreaRols
    - Responsables
    - Recomendaciones
    - Hallazgo
    - HallazgoComentarios

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
        logger.error(f"ENDPOINT /company_data/save_evidence: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("/company_data/get_country_list")
@inject
async def getPaises(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of countries.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - PaisCode
    - TelefonoCode

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_country_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("/company_data/get_country_states")
@inject
async def getPaisEstados(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of states by country.
    Maybe a good idea to retrieve this info by each country is use a third party API.

    ## REQUEST
    - PaisCode

    ## RESPONSE
    - PaisCode
    - EstadoCode
    - EstadoName

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_country_states: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("/company_data/get_customer_provider_list")
@inject
async def getClienteProveedorList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of customers and providers.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber
    - IsCompany
    - Name
    - Tipo
    - ApellidoPaterno
    - ApellidoMaterno
    - TipoMovimiento
    - FechaMovimiento
    - Aviso
    - PaisCode
    - EstadoCode
    - EstadoNombre
    - Municipio
    - Localidad
    - Colonia
    - Calle
    - NumeroExterior
    - NumeroInterior
    - CP
    - Telefono

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_customer_provider_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("/company_data/save_customer_provider")
@inject
async def saveClienteProveedor(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save a customer or provider.

    ## REQUEST
    - ID
    - IsCompany
    - Name
    - Tipo
    - ApellidoPaterno
    - ApellidoMaterno
    - TipoMovimiento
    - FechaMovimiento
    - Aviso
    - PaisCode
    - EstadoCode
    - Municipio
    - Localidad
    - Colonia
    - Calle
    - NumeroExterior
    - NumeroInterior
    - CP
    - Telefono

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
        logger.error(f"ENDPOINT /company_data/get_customer_provider_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/get_provider_national_list")
@inject
async def getProveedorNacionalList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of national providers.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber
    - RFC
    - ValorOperaciones
    - Porcentaje
    - IsOpinionPositiva
    - IsOperacionesVirtuales
    - FechaMovimiento
    - Aviso
    - FechaAviso

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_provider_national_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_provider_national")
@inject
async def saveProveedorNacional(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of national providers.

    ## REQUEST
    - ID
    - RFC
    - ValorOperaciones
    - Porcentaje
    - IsOpinionPositiva
    - IsOperacionesVirtuales
    - FechaMovimiento
    - Aviso
    - FechaAviso

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
        logger.error(f"ENDPOINT /company_data/save_provider_national: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/get_type_caracter_list")
@inject
async def getCaracterTipos(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of national providers.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - Code
    - Description

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_type_caracter_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
@app.post("/company_data/get_shareholder_partner_list")
@inject
async def getSocioAccionistaList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of shareholders and partners.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber
    - IsCompany
    - Nombre
    - RFC
    - CaracterCode
    - CaracterDescripcion
    - IsObligadoTributar
    - NombreEmpresa
    - TipoMovimiento
    - EscrituraPublica
    - FechaEscritura
    - Fedatario
    - NumeroNotario
    - EfectoEscrituraPublica
    - Aviso
    - FechaAviso

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_shareholder_partner_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_shareholder_partner")
@inject
async def saveSocioAccionista(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save a shareholder or partner.

    ## REQUEST
    - ID
    - IsCompany
    - Nombre
    - RFC
    - CaracterCode
    - IsObligadoTributar
    - NombreEmpresa
    - TipoMovimiento
    - EscrituraPublica
    - FechaEscritura
    - Fedatario
    - NumeroNotario
    - EfectoEscrituraPublica
    - Aviso
    - FechaAviso

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
        logger.error(f"ENDPOINT /company_data/get_shareholder_partner_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )


@app.post("/company_data/get_legal_use_list")
@inject
async def getLegalUsoList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of legal uses.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber
    - DomicilioAcreditacion
        - Arrendador
        - Aviso
        - Calle
        - Colonia
        - CP
        - Municipio
        - EstadoCode
        - EstadoNombre
        - PaisCode
        - Localidad
        - NumeroExterior
        - NumeroInterior
        - Arrendatario
        - FechaAviso
        - FechaInicioVigencia
        - FechaVencimiento
    - DomicilioNuevo
        - Arrendador
        - Aviso
        - Calle
        - Colonia
        - CP
        - Municipio
        - EstadoCode
        - EstadoNombre
        - PaisCode
        - Localidad
        - NumeroExterior
        - NumeroInterior
        - Arrendatario
        - FechaAviso
        - FechaInicioVigencia
        - FechaVencimiento
        - RatificarDomicilio
        - RFC
        - TipoDocumento

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_legal_use_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    
    
@app.post("/company_data/save_legal_use")
@inject
async def saveLegalUso(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a legal use.

    ## REQUEST
    - DomicilioAcreditacion
        - Arrendador
        - Aviso
        - Calle
        - Colonia
        - CP
        - Municipio
        - EstadoCode
        - EstadoNombre
        - PaisCode
        - Localidad
        - NumeroExterior
        - NumeroInterior
        - Arrendatario
        - FechaAviso
        - FechaInicioVigencia
        - FechaVencimiento
    - DomicilioNuevo
        - Arrendador
        - Aviso
        - Calle
        - Colonia
        - CP
        - Municipio
        - EstadoCode
        - EstadoNombre
        - PaisCode
        - Localidad
        - NumeroExterior
        - NumeroInterior
        - Arrendatario
        - FechaAviso
        - FechaInicioVigencia
        - FechaVencimiento
        - RatificarDomicilio
        - RFC
        - TipoDocumento

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
        logger.error(f"ENDPOINT /company_data/get_legal_use: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/get_operative_links_list")
@inject
async def getEnlacesOperativosList(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of operative links.

    ## REQUEST
    - Empty Request

    ## RESPONSE
    - ID
    - CaseNumber

    """

    try:
        
        return ApiResponse(
            Status="200",
            Message="Not Implemented",
            Data=None,
            Token=user_data.token
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /company_data/get_operative_links_list: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_operative_link")
@inject
async def saveEnlaceOperativo(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save an operative link.

    ## REQUEST
    - ID

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
        logger.error(f"ENDPOINT /company_data/save_operative_link: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

@app.post("/company_data/save_operative_link")
@inject
async def saveEnlaceOperativo(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to save an operative link.

    ## REQUEST
    - ID

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
        logger.error(f"ENDPOINT /company_data/save_operative_link: {str(e)}")
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )
    

