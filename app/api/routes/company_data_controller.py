from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject
from datetime import datetime

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse

from app.schemas.company_data.request import (
    SectionDatosEmpresaListRequest,
    RazonSocialHistoricoRequest,
    RazonSocialSaveRequest,
    DatosEmpresaHallazgosListRequest,
    DatosempresaEvidenciaIDRequest,
    DatosEmpresaEvidenciaSaveRequest,
    PaisesRequest,
    EstadosRequest,
    ClienteProveedorHistoricoRequest,
    ClienteProveedorSaveRequest,
    ProveedorNacionalHistoricoRequest,
    ProveedorNacionalSaveRequest,
    CaracterTiposRequest,
    SocioAccionistaHistoricoRequest,
    SocioAccionistaSaveRequest,
    LegalUsoHistoricoRequest,
    LegalUsoSaveRequest,
    EnlacesOperativosHistoricoRequest,
    EnlaceOperativoSaveRequest,
)

from app.services.company_data.company_data_services import *

from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger

app = APIRouter()
security = HTTPBearer()


@app.post("/getSectionList")
@inject
async def getSectionList(
    request: SectionDatosEmpresaListRequest,
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
    - Selected

    """

    logger.info(f"ENDPOINT /getSectionList: {request}")

    try:

        logger.info("Fetching section list")

        response, token = await fetch_section_list(
            date_ini=request.DateIni,
            date_end=request.DateEnd,
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=response,
            token=token,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /getSectionList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=None,
            token=None,
        )


@app.post("/getRazonSocialHistoricoList")
@inject
async def getRazonSocialHistoricoList(
    request: RazonSocialHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getRazonSocialHistoricoList: {request}")

    try:

        logger.info("Fetching social reason history list")

        data, token = await fetch_razon_social_historico_list(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getRazonSocialHistoricoList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=None,
            token=None,
        )


@app.post("/saveRazonSocial")
@inject
async def saveRazonSocial(
    request: RazonSocialSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveRazonSocial: {request}")

    try:
        response = await save_razon_social(
            request=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=user_data.token,
            )
        
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /getRazonSocial: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getHallazgosList")
@inject
async def getHallazgosList(
    request: DatosEmpresaHallazgosListRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getHallazgosList: {request}")

    try:

        data, token = await fetch_hallazgos_list(
            code_section=request.CodeSection,
            token=user_data.token,
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
            message="Se presentó un error",
            data=None,
            token=None,
        )


@app.post("/getEvidenciaID")
@inject
async def getEvidenciaID(
    request: DatosempresaEvidenciaIDRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getEvidenciaID: {request}")

    try:

        response, token = await fetch_evidencia_id(
            id=request.id,
            code_section=request.codeSection,
            token=user_data.token,
        )
        
        return ApiResponse(
            success=True,
            message="OK",
            data=response,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getEvidenciaID: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveEvidencia")
@inject
async def saveEvidencia(
    request: DatosEmpresaEvidenciaSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveEvidencia: {request}")

    try:

        response = await save_evidencia(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            logger.info(f"ENDPOINT /saveEvidencia: success response")
            return ApiResponse(
                success=True,
                message="OK",
                data=None,
                token=None,
            )

        logger.error("ENDPOINT /saveEvidencia: unexpected status code")
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=None,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /saveEvidencia: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getPaises")
@inject
async def getPaises(
    request: PaisesRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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
        logger.info("ENDPOINT /getPaises")

        data, token = await fetch_paises(
            token=user_data.token,
        )


        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getPaises: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getPaisEstados")
@inject
async def getPaisEstados(
    request: EstadosRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

        logger.info("ENDPOINT /getPaisEstados")

        data, token = await fetch_paises_estados(
            iid_pais=request.idPais,
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getPaisEstados: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getClienteProveedorList")
@inject
async def getClienteProveedorList(
    requwst: ClienteProveedorHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

        logger.info("ENDPOINT /getClienteProveedorList")

        data, token = await fetch_cliente_proveedor_list(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getClienteProveedorList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveClienteProveedor")
@inject
async def saveClienteProveedor(
    request: ClienteProveedorSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveClienteProveedor: {request}")

    try:

        response = await save_cliente_proveedor(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            logger.info(f"ENDPOINT /saveClienteProveedor: success response")
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=None,
            )
        
        return ApiResponse(
            success=True,
            message="OK",
            data=True,
            token=None,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /saveClienteProveedor: {e}")
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=None,
        )


@app.post("/getProveedorNacionalList")
@inject
async def getProveedorNacionalList(
    request: ProveedorNacionalHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getProveedorNacionalList: {request}")

    try:

        data, token = await fetch_provedor_nacional_list(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="Fetched national providers successfully",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getProveedorNacionalList: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveProveedorNacional")
@inject
async def saveProveedorNacional(
    request: ProveedorNacionalSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveProveedorNacional: {request}")

    try:

        response = await save_provedor_nacional(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=user_data.token,
            )

        return ApiResponse(
            success=True,
            message="OK",
            data=True,
            token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /saveProveedorNacional: {str(e)}")
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=user_data.token,
        )


@app.post("/getCaracterTipos")
@inject
async def getCaracterTipos(
    request: CaracterTiposRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getCaracterTipos: {request}")

    try:

        data, token = await fetch_caracter_tipos(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getCaracterTipos: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getSocioAccionistaList")
@inject
async def getSocioAccionistaList(
    request: SocioAccionistaHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getSocioAccionistaList: {request}")

    try:
        data, token = await fetch_socio_accionista_list(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /getSocioAccionistaList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveSocioAccionista")
@inject
async def saveSocioAccionista(
    request: SocioAccionistaSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveSocioAccionista: {request}")

    try:
        response = await save_socio_accionista(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            logger.info(f"ENDPOINT /saveSocioAccionista: success response")
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=user_data.token,
            )

        return ApiResponse(
            success=False,
            message="Failed to save socio accionista",
            data=False,
            token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /saveSocioAccionista: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getLegalUsoList")
@inject
async def getLegalUsoList(
    request: LegalUsoHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /getLegalUsoList: {request}")

    try:

        data, token = await fetch_legal_uso_list(
            token=user_data.token,
        )
    
        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getLegalUsoList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveLegalUso")
@inject
async def saveLegalUso(
    request: LegalUsoSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveLegalUso: {request}")

    try:

        response = await save_legal_uso(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=None,
            )
        
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=None,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /saveLegalUso: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/getEnlacesOperativosList")
@inject
async def getEnlacesOperativosList(
    request: EnlacesOperativosHistoricoRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

        logger.info("ENDPOINT /getEnlacesOperativosList")

        data, token = await fetch_enlaces_operativos_list(
            token=user_data.token,
        )

        return ApiResponse(
            success=True,
            message="OK",
            data=data,
            token=token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getEnlacesOperativosList: {str(e)}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )


@app.post("/saveEnlaceOperativo")
@inject
async def saveEnlaceOperativo(
    request: EnlaceOperativoSaveRequest,
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["Admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
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

    logger.info(f"ENDPOINT /saveEnlaceOperativo: {request}")

    try:

        response = await save_enlace_operativo(
            data=request,
            token=user_data.token,
        )

        if response.status_code == 200:
            logger.info(f"ENDPOINT /saveEnlaceOperativo: success response")
            return ApiResponse(
                success=True,
                message="OK",
                data=True,
                token=None,
            )
        
        return ApiResponse(
            success=False,
            message="Se presentó un error",
            data=False,
            token=None,
        )
    
    except Exception as e:
        logger.error(f"ENDPOINT /saveEnlaceOperativo: {e}")
        return ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
            token=None,
        )
