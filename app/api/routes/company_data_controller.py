from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject
from datetime import datetime

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse

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

from app.schemas.models import (
    HallazgoOptionModel,
    AreaRolModel,
    DatosEmpresaSocioAccionistaCaracterModel,
    PaisModel,
    PaisEstadoModel,
    DatosEmpresaLegalUsoModel,

)

from app.services.get_requirement_obligation import get_requerimiento_obligaciones
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

    logger.info(f"ENDPOINT /getSectionList: {request}")

    # data = [
    #     SectionOptionDatosEmpresaResponse(Code="RazonSocial", Cantidad=0, Total=11, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="Domicilio", Cantidad=0, Total=29, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="ClienteExtranjero", Cantidad=3, Total=15, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="ProveedorNacional", Cantidad=7, Total=10, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="SociosAccionistas", Cantidad=2, Total=8, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="LegalUso", Cantidad=9, Total=20, Selected=False),
    #     SectionOptionDatosEmpresaResponse(Code="EnlacesOperativos", Cantidad=4, Total=4, Selected=False),
    # ]

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

    logger.info(f"ENDPOINT /getRazonSocialHistoricoList: {request}")

    # data = [
    #     HistoricoResponse(
    #         Status="Modificado",
    #         Usuario="Usuario 1",
    #         Fecha=datetime.utcnow(),
    #         Data=RazonSocialResponse(
    #             ID=1,
    #             CaseNumber=1,
    #             Name="Razón Social 1",
    #             RFC="RFC 1",
    #             Folio="Folio 1",
    #             MovementDate=datetime.utcnow(),
    #             DeedDate=datetime.utcnow(),
    #             Fedatario="Fedatario 1",
    #             Notary="Notario 1",
    #             Effect="Estatutos",
    #             Notice="Aviso 1",
    #             NoticeDate=datetime.utcnow(),
    #             IsCompany=True
    #         )
    #     ),
    #     HistoricoResponse(
    #         Status="Vigente",
    #         Usuario="Usuario 2",
    #         Fecha=datetime.utcnow(),
    #         Data=RazonSocialResponse(
    #             ID=2,
    #             CaseNumber=2,
    #             Name="Razón Social 2",
    #             RFC="RFC 2",
    #             Folio="Folio 2",
    #             MovementDate=datetime.utcnow(),
    #             DeedDate=datetime.utcnow(),
    #             Fedatario="Fedatario 2",
    #             Notary="Notario 2",
    #             Effect="Fusion",
    #             Notice="Aviso 2",
    #             NoticeDate=datetime.utcnow(),
    #             IsCompany=False
    #         )
    #     )
    # ]

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

    logger.info(f"ENDPOINT /saveRazonSocial: {request}")

    # data = RazonSocialResponse(
    #     ID=1,
    #     CaseNumber=1,
    #     Name="Razón Social 1",
    #     RFC="RFC 1",
    #     Folio="Folio 1",
    #     MovementDate="2023-01-01T00:00:00",
    #     DeedDate="2023-01-02T00:00:00",
    #     Fedatario="Fedatario 1",
    #     Notary="Notario 1",
    #     Effect="Estatutos",
    #     Notice="Aviso 1",
    #     NoticeDate="2023-01-03T00:00:00",
    #     IsCompany=True,
    # )

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

    logger.info(f"ENDPOINT /getHallazgosList: {request}")

    try:
        # data = [
        #     HallazgoOptionModel(ID=1, Code="Code 1", Nombre="Hallazgo 01"),
        #     HallazgoOptionModel(ID=2, Code="Code 2", Nombre="Hallazgo 02"),
        #     HallazgoOptionModel(ID=3, Code="Code 3", Nombre="Hallazgo 03"),
        #     HallazgoOptionModel(ID=4, Code="Code 4", Nombre="Hallazgo 04"),
        # ]

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

    logger.info(f"ENDPOINT /getEvidenciaID: {request}")

    try:
        # evidencia = DatosEmpresaEvidenciaResponse(
        #     ID=request.ID,
        #     CaseNumber=request.ID,
        #     AreaRols=None,
        #     Responsables=None,
        #     Cliente="Traders",
        #     Fecha=datetime.utcnow(),
        #     Recomendaciones=None,
        #     Hallazgo=None,
        # )

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
        # data = [
        #     HistoricoResponse(
        #         Status="Modificado",
        #         Usuario="Usuario 1",
        #         Fecha="2025-01-07T00:00:00",
        #         Data=ClienteProveedorResponse(
        #             ID=1,
        #             CaseNumber=1,
        #             IsCompany=True,
        #             Name="Razón Social 1",
        #             Tipo="Cliente",
        #             ApellidoPaterno="Apellido Paterno 1",
        #             ApellidoMaterno="Apellido Materno 1",
        #             TipoMovimiento="Alta",
        #             Aviso="Aviso 1",
        #             Municipio="Municipio 1",
        #             EstadoCode="cod1",
        #             EstadoNombre="Estado 1",
        #             PaisCode="MX",
        #             FechaMovimiento="2025-01-07T00:00:00",
        #         ),
        #     ),
        #     HistoricoResponse(
        #         Status="Modificado",
        #         Usuario="Usuario 2",
        #         Fecha="2025-01-07T00:00:00",
        #         Data=ClienteProveedorResponse(
        #             ID=2,
        #             CaseNumber=2,
        #             IsCompany=False,
        #             Name="Razón Social 2",
        #             Tipo="Proveedor",
        #             ApellidoPaterno="Apellido Paterno 2",
        #             ApellidoMaterno="Apellido Materno 2",
        #             TipoMovimiento="Baja",
        #             Aviso="Aviso 2",
        #             Municipio="Municipio 2",
        #             EstadoCode="cod2",
        #             EstadoNombre="Estado 2",
        #             PaisCode="MX",
        #             FechaMovimiento="2025-01-07T00:00:00",
        #         ),
        #     ),
        # ]

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

    logger.info(f"ENDPOINT /saveClienteProveedor: {request}")

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=True,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /saveClienteProveedor: {e}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getProveedorNacionalList")
@inject
async def getProveedorNacionalList(
    request: ProveedorNacionalHistoricoRequest,
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

    logger.info(f"ENDPOINT /getProveedorNacionalList: {request}")

    try:
        data = [
            ProveedorNacionalResponse(
                ID=1,
                Name="Proveedor 1",
                IsActive=True,
                PaisCode="MX",
                EstadoCode="NL",
            ),
            ProveedorNacionalResponse(
                ID=2,
                Name="Proveedor 2",
                IsActive=True,
                PaisCode="MX",
                EstadoCode="JAL",
            ),
        ]

        return ApiResponse(
            Success=True,
            Message="Fetched national providers successfully",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getProveedorNacionalList: {e}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/saveProveedorNacional")
@inject
async def saveProveedorNacional(
    request: ProveedorNacionalSaveRequest,
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

    logger.info(f"ENDPOINT /saveProveedorNacional: {request}")

    try:
        return ApiResponse(
            Success=True,  # Corregido de "Status" a "Success"
            Message="OK",
            Data=True,
            Token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /saveProveedorNacional: {str(e)}")
        return ApiResponse(
            Success=False,  # Corregido de "Status" a "Success"
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getCaracterTipos")
@inject
async def getCaracterTipos(
    request: CaracterTiposRequest,
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

    logger.info(f"ENDPOINT /getCaracterTipos: {request}")

    try:
        data = [
            DatosEmpresaSocioAccionistaCaracterModel(Code="socio", Description="Socio"),
            DatosEmpresaSocioAccionistaCaracterModel(Code="accionista", Description="Accionista"),
            DatosEmpresaSocioAccionistaCaracterModel(Code="mconsejo", Description="Miembro del consejo"),
        ]
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getCaracterTipos: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getSocioAccionistaList")
@inject
async def getSocioAccionistaList(
    request: SocioAccionistaHistoricoRequest,
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

    logger.info(f"ENDPOINT /getSocioAccionistaList: {request}")

    data = [
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 1",
            Fecha="2024-01-01T00:00:00",
            Data=SocioAccionistaResponse(
                ID=1,
                CaseNumber=1,
                RFC="RFC 1",
                CaracterCode="socio",
                CaracterDescripcion="Socio",
                TipoMovimiento="Agregar",
                EscrituraPublica=11,
                FechaEscritura="2024-01-01T00:00:00",
                IsCompany=True,
                IsObligadoTributar=False,
                Nombre="Nombre 1",
                NombreEmpresa="Empresa 1",
            ),
        ),
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 2",
            Fecha="2024-01-01T00:00:00",
            Data=SocioAccionistaResponse(
                ID=2,
                CaseNumber=3,
                RFC="RFC 3",
                CaracterCode="accionista",
                CaracterDescripcion="Accionista",
                TipoMovimiento="Ratificar",
                EscrituraPublica=110,
                FechaEscritura="2024-01-01T00:00:00",
                IsCompany=False,
                IsObligadoTributar=True,
                Nombre="Nombre 3",
                NombreEmpresa="Empresa 3",
            ),
        ),
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=ListResponse(
                Data=data,
                TotalRecords=len(data),
                CurrentPage=1,
                PageSize=len(data),
                TotalPages=1,
            ),
            Token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /getSocioAccionistaList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/saveSocioAccionista")
@inject
async def saveSocioAccionista(
    request: SocioAccionistaSaveRequest,
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

    logger.info(f"ENDPOINT /saveSocioAccionista: {request}")

    try:
        success = True
        message = "OK"
        data = True

        return ApiResponse(
            Success=success,
            Message=message,
            Data=data,
            Token=user_data.token,
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

    logger.info(f"ENDPOINT /getLegalUsoList: {request}")

    try:
        data = [
            HistoricoResponse(
                Status="Modificado",
                Usuario="Usuario 1",
                Fecha="2024-01-01T12:00:00",
                Data=LegalUsoResponse(
                    ID=1,
                    CaseNumber=1,
                    DomicilioAcreditacion=DatosEmpresaLegalUsoModel(
                        Calle="Calle 1",
                        Colonia="Colonia 1",
                        CP="12345",
                        Municipio="Municipio 1",
                        EstadoCode="cod1",
                        EstadoNombre="Estado 1",
                        PaisCode="MX",
                        Localidad="Localidad 1",
                        NumeroExterior="Numero Exterior 1",
                        NumeroInterior="Numero Interior 1",
                        FechaInicioVigencia="2024-01-01T12:00:00",
                    ),
                    DomicilioNuevo=DatosEmpresaLegalUsoModel(
                        Calle="Nuevo Calle 1",
                        Colonia="Nuevo Colonia 1",
                        CP="123",
                        Municipio="Nuevo Municipio 1",
                        EstadoCode="cod2",
                        EstadoNombre="Estado 2",
                        PaisCode="CO",
                        Localidad="Nuevo Localidad 1",
                        NumeroExterior="Nuevo Numero Exterior 1",
                        FechaInicioVigencia="2024-01-01T12:00:00",
                        TipoDocumento=2
                    )
                )
            ),
            HistoricoResponse(
                Status="Modificado",
                Usuario="Usuario 2",
                Fecha="2024-01-02T12:00:00",
                Data=LegalUsoResponse(
                    ID=2,
                    CaseNumber=3,
                    DomicilioAcreditacion=DatosEmpresaLegalUsoModel(
                        Calle="Calle 2",
                        Colonia="Colonia 2",
                        CP="12345",
                        Municipio="Municipio 2",
                        EstadoCode="cod2",
                        EstadoNombre="Estado 2",
                        PaisCode="MX",
                        Localidad="Localidad 2",
                        NumeroExterior="Numero Exterior 2",
                        NumeroInterior="Numero Interior 2",
                        FechaInicioVigencia="2024-01-02T12:00:00",
                    ),
                    DomicilioNuevo=DatosEmpresaLegalUsoModel(
                        Calle="Nuevo Calle 2",
                        Colonia="Nuevo Colonia 2",
                        CP="1232",
                        Municipio="Nuevo Municipio 2",
                        EstadoCode="cod3",
                        EstadoNombre="Estado 2",
                        PaisCode="US",
                        Localidad="Nuevo Localidad 2",
                        NumeroExterior="Nuevo Numero Exterior 2",
                        NumeroInterior="Nuevo Numero Interior 2",
                        FechaInicioVigencia="2024-01-02T12:00:00",
                        TipoDocumento=4
                    )
                )
            )
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=ListResponse(Data=data),
            Token=user_data.token
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getLegalUsoList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )



@app.post("/saveLegalUso")
@inject
async def saveLegalUso(
    request: LegalUsoSaveRequest,
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

    logger.info(f"ENDPOINT /saveLegalUso: {request}")

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=True,
            Token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /saveLegalUso: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getEnlacesOperativosList")
@inject
async def getEnlacesOperativosList(
    request: EnlacesOperativosHistoricoRequest,
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

    data = [
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 1",
            Fecha="2025-01-07T00:00:00",
            Data=EnlaceOperativoResponse(
                ID=1,
                CaseNumber=1,
                Nombre="Nombre 1",
                RFC="RFC 1",
                TipoRelacion="Relación 1",
                FechaInicio="2025-01-07T00:00:00",
                FechaFin="2025-01-07T00:00:00",
                Observaciones="Observaciones 1",
            ),
        ),
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 2",
            Fecha="2025-01-07T00:00:00",
            Data=EnlaceOperativoResponse(
                ID=2,
                CaseNumber=2,
                Nombre="Nombre 2",
                RFC="RFC 2",
                TipoRelacion="Relación 2",
                FechaInicio="2025-01-07T00:00:00",
                FechaFin="2025-01-07T00:00:00",
                Observaciones="Observaciones 2",
            ),
        ),
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=ListResponse(
                Data=data,
                CurrentPage=1,
                PageSize=10,
                TotalPages=1,
                TotalRecords=2,
            ),
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getEnlacesOperativosList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )



@app.post("/saveEnlaceOperativo")
@inject
async def saveEnlaceOperativo(
    request: EnlaceOperativoSaveRequest,
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

    logger.info(f"ENDPOINT /saveEnlaceOperativo: {request}")

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=True,
            Token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /saveEnlaceOperativo: {e}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


# @app.post("/saveEnlaceOperativo")
# @inject
# async def saveEnlaceOperativo(
#     _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
#     credentials: HTTPAuthorizationCredentials = Depends(security),
#     user_data: BaseData = Depends(get_current_user),
#     db_session: AsyncSession = Depends(get_db_session),
# ):
#     """
#     ## DESCRIPTION
#     ### Endpoint to save an operative link.

#     ## REQUEST
#     - ID

#     ## RESPONSE
#     - 200: Success
#     - 400: Bad Request
#     - 401: Unauthorized
#     - 403: Forbidden
#     - 500: Internal Server Error

#     """

#     try:
#         return ApiResponse(
#             Success=True,
#             Message="OK",
#             Data=True,
#             Token=user_data.token,
#         )
#     except Exception as e:
#         logger.error(f"ENDPOINT /saveEnlaceOperativo: {e}")
#         return ApiResponse(
#             Success=False,
#             Message="Se presentó un error",
#             Data=False,
#             Token=user_data.token,
#         )
