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
    PaginationBase,
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

    data = [
        SectionOptionDatosEmpresaResponse(Code="RazonSocial", Cantidad=0, Total=11, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="Domicilio", Cantidad=0, Total=29, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="ClienteExtranjero", Cantidad=3, Total=15, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="ProveedorNacional", Cantidad=7, Total=10, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="SociosAccionistas", Cantidad=2, Total=8, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="LegalUso", Cantidad=9, Total=20, Selected=False),
        SectionOptionDatosEmpresaResponse(Code="EnlacesOperativos", Cantidad=4, Total=4, Selected=False),
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=ListResponse(
                CurrentPage=0,
                PageSize=0,
                TotalPages=0,
                TotalRecords=0,
                Data=data,
            ),
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getSectionList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getRazonSocialHistoricoList")
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

    data = [
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 1",
            Fecha=datetime.utcnow(),
            Data=RazonSocialResponse(
                ID=1,
                CaseNumber=1,
                Name="Razón Social 1",
                RFC="RFC 1",
                Folio="Folio 1",
                MovementDate=datetime.utcnow(),
                DeedDate=datetime.utcnow(),
                Fedatario="Fedatario 1",
                Notary="Notario 1",
                Effect="Estatutos",
                Notice="Aviso 1",
                NoticeDate=datetime.utcnow(),
                IsCompany=True
            )
        ),
        HistoricoResponse(
            Status="Vigente",
            Usuario="Usuario 2",
            Fecha=datetime.utcnow(),
            Data=RazonSocialResponse(
                ID=2,
                CaseNumber=2,
                Name="Razón Social 2",
                RFC="RFC 2",
                Folio="Folio 2",
                MovementDate=datetime.utcnow(),
                DeedDate=datetime.utcnow(),
                Fedatario="Fedatario 2",
                Notary="Notario 2",
                Effect="Fusion",
                Notice="Aviso 2",
                NoticeDate=datetime.utcnow(),
                IsCompany=False
            )
        )
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=ListResponse(
                CurrentPage=1,
                PageSize=10,
                TotalPages=1,
                TotalRecords=len(data),
                Data=data
            ),
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getRazonSocialHistoricoList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getRazonSocial")
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

    data = RazonSocialResponse(
        ID=1,
        CaseNumber=1,
        Name="Razón Social 1",
        RFC="RFC 1",
        Folio="Folio 1",
        MovementDate="2023-01-01T00:00:00",
        DeedDate="2023-01-02T00:00:00",
        Fedatario="Fedatario 1",
        Notary="Notario 1",
        Effect="Estatutos",
        Notice="Aviso 1",
        NoticeDate="2023-01-03T00:00:00",
        IsCompany=True,
    )
    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getRazonSocial: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getHallazgosList")
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
        data = [
            HallazgoOptionModel(ID=1, Code="Code 1", Nombre="Hallazgo 01"),
            HallazgoOptionModel(ID=2, Code="Code 2", Nombre="Hallazgo 02"),
            HallazgoOptionModel(ID=3, Code="Code 3", Nombre="Hallazgo 03"),
            HallazgoOptionModel(ID=4, Code="Code 4", Nombre="Hallazgo 04"),
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=PaginationBase(
                Data=data,
                CurrentPage=1,
                PageSize=len(data),
                TotalPages=1,
                TotalRecords=len(data),
            ),
            Token=user_data.token,
        )
    except Exception as e:
        logger.error(f"ENDPOINT /getHallazgosList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getEvidenciaID")
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
        evidencia = DatosEmpresaEvidenciaResponse(
            ID=request.ID,
            CaseNumber=request.ID,
            AreaRols=None,
            Responsables=None,
            Cliente="Traders",
            Fecha=datetime.utcnow(),
            Recomendaciones=None,
            Hallazgo=None,
        )
        
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=evidencia,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getEvidenciaID: {e}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/saveEvidencia")
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
            Success=True,
            Message="OK",
            Data=True,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /saveEvidencia: {e}")
        return ApiResponse(
            Success=False,
            Message="Se presentó un error",
            Data=False,
            Token=user_data.token,
        )


@app.post("/getPaises")
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
        data = [
            PaisModel(PaisCode="AF", TelefonoCode="+93"),
            PaisModel(PaisCode="AL", TelefonoCode="+355"),
            PaisModel(PaisCode="DE", TelefonoCode="+49"),
            PaisModel(PaisCode="DZ", TelefonoCode="+213"),
            PaisModel(PaisCode="AD", TelefonoCode="+376"),
            PaisModel(PaisCode="AO", TelefonoCode="+244"),
            PaisModel(PaisCode="SA", TelefonoCode="+966"),
            PaisModel(PaisCode="AR", TelefonoCode="+54"),
            PaisModel(PaisCode="AM", TelefonoCode="+374"),
            PaisModel(PaisCode="AU", TelefonoCode="+61"),
            PaisModel(PaisCode="AT", TelefonoCode="+43"),
            PaisModel(PaisCode="AZ", TelefonoCode="+994"),
            PaisModel(PaisCode="BS", TelefonoCode="+1-242"),
            PaisModel(PaisCode="BD", TelefonoCode="+880"),
            PaisModel(PaisCode="BB", TelefonoCode="+1-246"),
            PaisModel(PaisCode="BH", TelefonoCode="+973"),
            PaisModel(PaisCode="BE", TelefonoCode="+32"),
            PaisModel(PaisCode="BZ", TelefonoCode="+501"),
            PaisModel(PaisCode="BJ", TelefonoCode="+229"),
            PaisModel(PaisCode="BY", TelefonoCode="+375"),
            PaisModel(PaisCode="MM", TelefonoCode="+95"),
            PaisModel(PaisCode="BO", TelefonoCode="+591"),
            PaisModel(PaisCode="BW", TelefonoCode="+267"),
            PaisModel(PaisCode="BR", TelefonoCode="+55"),
            PaisModel(PaisCode="BN", TelefonoCode="+673"),
            PaisModel(PaisCode="BG", TelefonoCode="+359"),
            PaisModel(PaisCode="BF", TelefonoCode="+226"),
            PaisModel(PaisCode="BI", TelefonoCode="+257"),
            PaisModel(PaisCode="BT", TelefonoCode="+975"),
            PaisModel(PaisCode="CV", TelefonoCode="+238"),
            PaisModel(PaisCode="KH", TelefonoCode="+855"),
            PaisModel(PaisCode="CM", TelefonoCode="+237"),
            PaisModel(PaisCode="CA", TelefonoCode="+1"),
            PaisModel(PaisCode="TD", TelefonoCode="+235"),
            PaisModel(PaisCode="CL", TelefonoCode="+56"),
            PaisModel(PaisCode="CN", TelefonoCode="+86"),
            PaisModel(PaisCode="CY", TelefonoCode="+357"),
            PaisModel(PaisCode="CO", TelefonoCode="+57"),
            PaisModel(PaisCode="KM", TelefonoCode="+269"),
            PaisModel(PaisCode="KP", TelefonoCode="+850"),
            PaisModel(PaisCode="KR", TelefonoCode="+82"),
            PaisModel(PaisCode="CI", TelefonoCode="+225"),
            PaisModel(PaisCode="CR", TelefonoCode="+506"),
            PaisModel(PaisCode="HR", TelefonoCode="+385"),
            PaisModel(PaisCode="CU", TelefonoCode="+53"),
            PaisModel(PaisCode="DK", TelefonoCode="+45"),
            PaisModel(PaisCode="DM", TelefonoCode="+1-767"),
            PaisModel(PaisCode="EC", TelefonoCode="+593"),
            PaisModel(PaisCode="EG", TelefonoCode="+20"),
            PaisModel(PaisCode="SV", TelefonoCode="+503"),
            PaisModel(PaisCode="AE", TelefonoCode="+971"),
            PaisModel(PaisCode="ER", TelefonoCode="+291"),
            PaisModel(PaisCode="SK", TelefonoCode="+421"),
            PaisModel(PaisCode="ES", TelefonoCode="+34"),
            PaisModel(PaisCode="US", TelefonoCode="+1"),
            PaisModel(PaisCode="EE", TelefonoCode="+372"),
            PaisModel(PaisCode="ET", TelefonoCode="+251"),
            PaisModel(PaisCode="FJ", TelefonoCode="+679"),
            PaisModel(PaisCode="PH", TelefonoCode="+63"),
            PaisModel(PaisCode="FI", TelefonoCode="+358"),
            PaisModel(PaisCode="FR", TelefonoCode="+33"),
            PaisModel(PaisCode="GA", TelefonoCode="+241"),
            PaisModel(PaisCode="GM", TelefonoCode="+220"),
            PaisModel(PaisCode="GE", TelefonoCode="+995"),
            PaisModel(PaisCode="GH", TelefonoCode="+233"),
            PaisModel(PaisCode="GD", TelefonoCode="+1-473"),
            PaisModel(PaisCode="GR", TelefonoCode="+30"),
            PaisModel(PaisCode="GT", TelefonoCode="+502"),
            PaisModel(PaisCode="GQ", TelefonoCode="+240"),
            PaisModel(PaisCode="GW", TelefonoCode="+245"),
            PaisModel(PaisCode="GN", TelefonoCode="+224"),
            PaisModel(PaisCode="GY", TelefonoCode="+592"),
            PaisModel(PaisCode="HT", TelefonoCode="+509"),
            PaisModel(PaisCode="HN", TelefonoCode="+504"),
            PaisModel(PaisCode="HU", TelefonoCode="+36"),
            PaisModel(PaisCode="IN", TelefonoCode="+91"),
            PaisModel(PaisCode="ID", TelefonoCode="+62"),
            PaisModel(PaisCode="IR", TelefonoCode="+98"),
            PaisModel(PaisCode="IQ", TelefonoCode="+964"),
            PaisModel(PaisCode="IE", TelefonoCode="+353"),
            PaisModel(PaisCode="IS", TelefonoCode="+354"),
            PaisModel(PaisCode="MH", TelefonoCode="+692"),
            PaisModel(PaisCode="SB", TelefonoCode="+677"),
            PaisModel(PaisCode="IL", TelefonoCode="+972"),
            PaisModel(PaisCode="IT", TelefonoCode="+39"),
            PaisModel(PaisCode="JM", TelefonoCode="+1-876"),
            PaisModel(PaisCode="JP", TelefonoCode="+81"),
            PaisModel(PaisCode="JO", TelefonoCode="+962"),
            PaisModel(PaisCode="KZ", TelefonoCode="+7"),
            PaisModel(PaisCode="KE", TelefonoCode="+254"),
            PaisModel(PaisCode="KG", TelefonoCode="+996"),
            PaisModel(PaisCode="KI", TelefonoCode="+686"),
            PaisModel(PaisCode="KW", TelefonoCode="+965"),
            PaisModel(PaisCode="LA", TelefonoCode="+856"),
            PaisModel(PaisCode="LS", TelefonoCode="+266"),
            PaisModel(PaisCode="LV", TelefonoCode="+371"),
            PaisModel(PaisCode="LB", TelefonoCode="+961"),
            PaisModel(PaisCode="LR", TelefonoCode="+231"),
            PaisModel(PaisCode="LY", TelefonoCode="+218"),
            PaisModel(PaisCode="LI", TelefonoCode="+423"),
            PaisModel(PaisCode="LT", TelefonoCode="+370"),
            PaisModel(PaisCode="LU", TelefonoCode="+352"),
            PaisModel(PaisCode="MK", TelefonoCode="+389"),
            PaisModel(PaisCode="MG", TelefonoCode="+261"),
            PaisModel(PaisCode="MY", TelefonoCode="+60"),
            PaisModel(PaisCode="MW", TelefonoCode="+265"),
            PaisModel(PaisCode="MV", TelefonoCode="+960"),
            PaisModel(PaisCode="ML", TelefonoCode="+223"),
            PaisModel(PaisCode="MT", TelefonoCode="+356"),
            PaisModel(PaisCode="MA", TelefonoCode="+212"),
            PaisModel(PaisCode="MU", TelefonoCode="+230"),
            PaisModel(PaisCode="MR", TelefonoCode="+222"),
            PaisModel(PaisCode="MX", TelefonoCode="+52"),
            PaisModel(PaisCode="FM", TelefonoCode="+691"),
            PaisModel(PaisCode="MD", TelefonoCode="+373"),
            PaisModel(PaisCode="MC", TelefonoCode="+377"),
            PaisModel(PaisCode="MN", TelefonoCode="+976"),
            PaisModel(PaisCode="ME", TelefonoCode="+382"),
            PaisModel(PaisCode="MZ", TelefonoCode="+258"),
            PaisModel(PaisCode="NA", TelefonoCode="+264"),
            PaisModel(PaisCode="NR", TelefonoCode="+674"),
            PaisModel(PaisCode="NP", TelefonoCode="+977"),
            PaisModel(PaisCode="NI", TelefonoCode="+505"),
            PaisModel(PaisCode="NE", TelefonoCode="+227"),
            PaisModel(PaisCode="NG", TelefonoCode="+234"),
            PaisModel(PaisCode="NO", TelefonoCode="+47"),
            PaisModel(PaisCode="NZ", TelefonoCode="+64"),
            PaisModel(PaisCode="NL", TelefonoCode="+31"),
            PaisModel(PaisCode="PK", TelefonoCode="+92"),
            PaisModel(PaisCode="PW", TelefonoCode="+680"),
            PaisModel(PaisCode="PA", TelefonoCode="+507"),
            PaisModel(PaisCode="PG", TelefonoCode="+675"),
            PaisModel(PaisCode="PY", TelefonoCode="+595"),
            PaisModel(PaisCode="PE", TelefonoCode="+51"),
            PaisModel(PaisCode="PL", TelefonoCode="+48"),
            PaisModel(PaisCode="PT", TelefonoCode="+351"),
            PaisModel(PaisCode="GB", TelefonoCode="+44"),
            PaisModel(PaisCode="CZ", TelefonoCode="+420"),
            PaisModel(PaisCode="DO", TelefonoCode="+1-809"),
            PaisModel(PaisCode="RW", TelefonoCode="+250"),
            PaisModel(PaisCode="RO", TelefonoCode="+40"),
            PaisModel(PaisCode="RU", TelefonoCode="+7"),
            PaisModel(PaisCode="WS", TelefonoCode="+685"),
            PaisModel(PaisCode="KN", TelefonoCode="+1-869"),
            PaisModel(PaisCode="SM", TelefonoCode="+378"),
            PaisModel(PaisCode="VC", TelefonoCode="+1-784"),
            PaisModel(PaisCode="LC", TelefonoCode="+1-758"),
            PaisModel(PaisCode="ST", TelefonoCode="+239"),
            PaisModel(PaisCode="SN", TelefonoCode="+221"),
            PaisModel(PaisCode="RS", TelefonoCode="+381"),
            PaisModel(PaisCode="SC", TelefonoCode="+248"),
            PaisModel(PaisCode="SL", TelefonoCode="+232"),
            PaisModel(PaisCode="SG", TelefonoCode="+65"),
            PaisModel(PaisCode="SY", TelefonoCode="+963"),
            PaisModel(PaisCode="SO", TelefonoCode="+252"),
            PaisModel(PaisCode="LK", TelefonoCode="+94"),
            PaisModel(PaisCode="SZ", TelefonoCode="+268"),
            PaisModel(PaisCode="ZA", TelefonoCode="+27"),
            PaisModel(PaisCode="SS", TelefonoCode="+211"),
            PaisModel(PaisCode="SD", TelefonoCode="+249"),
            PaisModel(PaisCode="SE", TelefonoCode="+46"),
            PaisModel(PaisCode="CH", TelefonoCode="+41"),
            PaisModel(PaisCode="SR", TelefonoCode="+597"),
            PaisModel(PaisCode="TH", TelefonoCode="+66"),
            PaisModel(PaisCode="TW", TelefonoCode="+886"),
            PaisModel(PaisCode="TZ", TelefonoCode="+255"),
            PaisModel(PaisCode="TJ", TelefonoCode="+992"),
            PaisModel(PaisCode="TG", TelefonoCode="+228"),
            PaisModel(PaisCode="TO", TelefonoCode="+676"),
            PaisModel(PaisCode="TT", TelefonoCode="+1-868"),
            PaisModel(PaisCode="TN", TelefonoCode="+216"),
            PaisModel(PaisCode="TM", TelefonoCode="+993"),
            PaisModel(PaisCode="TR", TelefonoCode="+90"),
            PaisModel(PaisCode="TV", TelefonoCode="+688"),
            PaisModel(PaisCode="UA", TelefonoCode="+380"),
            PaisModel(PaisCode="UG", TelefonoCode="+256"),
            PaisModel(PaisCode="UY", TelefonoCode="+598"),
            PaisModel(PaisCode="UZ", TelefonoCode="+998"),
            PaisModel(PaisCode="VU", TelefonoCode="+678"),
            PaisModel(PaisCode="VA", TelefonoCode="+379"),
            PaisModel(PaisCode="VE", TelefonoCode="+58"),
            PaisModel(PaisCode="VN", TelefonoCode="+84"),
            PaisModel(PaisCode="YE", TelefonoCode="+967"),
            PaisModel(PaisCode="DJ", TelefonoCode="+253"),
            PaisModel(PaisCode="ZM", TelefonoCode="+260"),
            PaisModel(PaisCode="ZW", TelefonoCode="+263"),
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getPaises: {e}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getPaisEstados")
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

    from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.company_data.response import PaisEstadoModel
from app.services.role_checker import RoleChecker, get_current_user

from config.logger_config import logger

app = APIRouter()
security = HTTPBearer()

@app.post("/getPaisEstados")
@inject
async def getPaisEstados(
    request: dict,  # Replace with the specific request model if available
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a list of states by country.

    ## REQUEST
    - PaisCode: str

    ## RESPONSE
    - PaisCode: str
    - EstadoCode: str
    - EstadoName: str

    """

    try:
        data = [
            PaisEstadoModel(PaisCode=request.get("PaisCode"), EstadoCode="cod1", EstadoName=f"Estado 1 - {request.get('PaisCode')}"),
            PaisEstadoModel(PaisCode=request.get("PaisCode"), EstadoCode="cod2", EstadoName=f"Estado 2 - {request.get('PaisCode')}"),
            PaisEstadoModel(PaisCode=request.get("PaisCode"), EstadoCode="cod3", EstadoName=f"Estado 3 - {request.get('PaisCode')}"),
            PaisEstadoModel(PaisCode=request.get("PaisCode"), EstadoCode="cod4", EstadoName=f"Estado 4 - {request.get('PaisCode')}"),
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=data,
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getPaisEstados: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/getClienteProveedorList")
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
        data = [
            HistoricoResponse(
                Status="Modificado",
                Usuario="Usuario 1",
                Fecha="2025-01-07T00:00:00",
                Data=ClienteProveedorResponse(
                    ID=1,
                    CaseNumber=1,
                    Name="Razón Social 1",
                    IsCompany=True,
                    Aviso="Aviso 1",
                    Calle="Calle 1",
                    Colonia="Colonia 1",
                    CP="12345",
                    Municipio="Municipio 1",
                    Telefono="+52 123456",
                    EstadoCode="cod1",
                    EstadoNombre="Estado 1",
                    PaisCode="MX",
                    FechaMovimiento="2025-01-07T00:00:00",
                    Localidad="Localidad 1",
                    NumeroExterior="Numero Exterior 1",
                    NumeroInterior="Numero Interior 1",
                    Tipo="Cliente",
                    TipoMovimiento="Alta",
                ),
            ),
            HistoricoResponse(
                Status="Modificado",
                Usuario="Usuario 2",
                Fecha="2025-01-07T00:00:00",
                Data=ClienteProveedorResponse(
                    ID=2,
                    CaseNumber=3,
                    Name="Razón Social 2",
                    IsCompany=False,
                    Aviso="Aviso 2",
                    Calle="Calle 2",
                    Colonia="Colonia 2",
                    CP="54321",
                    Municipio="Municipio 2",
                    Telefono="+1 123456",
                    EstadoCode="cod2",
                    EstadoNombre="Estado 2",
                    PaisCode="MX",
                    FechaMovimiento="2025-01-07T00:00:00",
                    Localidad="Localidad 2",
                    NumeroExterior="Numero Exterior 2",
                    NumeroInterior="Numero Interior 2",
                    Tipo="Proveedor",
                    TipoMovimiento="Baja",
                    ApellidoMaterno="Apellido Materno 2",
                    ApellidoPaterno="Apellido Paterno 2",
                ),
            ),
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=PaginationBase(
                Data=data
            ),
            Token=user_data.token,
        )

    except Exception as e:
        logger.error(f"ENDPOINT /getClienteProveedorList: {str(e)}")
        return ApiResponse(
            Success=False,
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token,
        )


@app.post("/saveClienteProveedor")
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

    data = [
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 1",
            Fecha="2024-01-01T00:00:00",
            Data=SocioAccionistaResponse(
                ID=1,
                CaseNumber=1,
                Aviso="Aviso 1",
                FechaAviso="2024-01-01T00:00:00",
                RFC="RFC 1",
                CaracterCode="socio",
                CaracterDescripcion="Socio",
                TipoMovimiento="Agregar",
                EfectoEscrituraPublica="Fusion",
                EscrituraPublica=11,
                FechaEscritura="2024-01-01T00:00:00",
                Fedatario="Fedatario 1",
                IsCompany=True,
                IsObligadoTributar=False,
                Nombre="Nombre 1",
                NombreEmpresa="Empresa 1",
                NumeroNotario=12,
            ),
        ),
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 2",
            Fecha="2024-01-01T00:00:00",
            Data=SocioAccionistaResponse(
                ID=2,
                CaseNumber=3,
                Aviso="Aviso 3",
                FechaAviso="2024-01-01T00:00:00",
                RFC="RFC 3",
                CaracterCode="accionista",
                CaracterDescripcion="Accionista",
                TipoMovimiento="Ratificar",
                EfectoEscrituraPublica="CambioObjeto",
                EscrituraPublica=110,
                FechaEscritura="2024-01-01T00:00:00",
                Fedatario="Fedatario 3",
                IsCompany=False,
                IsObligadoTributar=True,
                Nombre="Nombre 3",
                NombreEmpresa="Empresa 3",
                NumeroNotario=120,
            ),
        ),
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=PaginationBase(
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
        data = [
            HistoricoResponse(
                Status="Modificado",
                Usuario="Usuario 1",
                Fecha="2024-01-01T12:00:00",
                Data=LegalUsoResponse(
                    ID=1,
                    CaseNumber=1,
                    DomicilioAcreditacion=DatosEmpresaLegalUsoModel(
                        Arrendador="Arrendador 1",
                        Aviso="Aviso 1",
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
                        Arrendatario="Arrendatario 1",
                        FechaAviso="2024-01-01T12:00:00",
                        FechaInicioVigencia="2024-01-01T12:00:00",
                        FechaVencimiento="2024-12-31T12:00:00"
                    ),
                    DomicilioNuevo=DatosEmpresaLegalUsoModel(
                        Arrendador="Nuevo Arrendador 1",
                        Aviso="Nuevo Aviso 1",
                        Calle="Nuevo Calle 1",
                        Colonia="Nuevo Colonia 1",
                        CP="123",
                        Municipio="Nuevo Municipio 1",
                        EstadoCode="cod2",
                        EstadoNombre="Estado 2",
                        PaisCode="CO",
                        Localidad="Nuevo Localidad 1",
                        NumeroExterior="Nuevo Numero Exterior 1",
                        NumeroInterior="Nuevo Numero Interior 1",
                        Arrendatario="Nuevo Arrendatario 1",
                        FechaAviso="2024-01-01T12:00:00",
                        FechaInicioVigencia="2024-01-01T12:00:00",
                        FechaVencimiento="2024-12-31T12:00:00",
                        RatificarDomicilio=False,
                        RFC="Nuevo RFC 1",
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
                        Arrendador="Arrendador 2",
                        Aviso="Aviso 2",
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
                        Arrendatario="Arrendatario 2",
                        FechaAviso="2024-01-02T12:00:00",
                        FechaInicioVigencia="2024-01-02T12:00:00",
                        FechaVencimiento="2024-12-31T12:00:00"
                    ),
                    DomicilioNuevo=DatosEmpresaLegalUsoModel(
                        Arrendador="Nuevo Arrendador 2",
                        Aviso="Nuevo Aviso 2",
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
                        Arrendatario="Nuevo Arrendatario 2",
                        FechaAviso="2024-01-02T12:00:00",
                        FechaInicioVigencia="2024-01-02T12:00:00",
                        FechaVencimiento="2024-12-31T12:00:00",
                        RatificarDomicilio=True,
                        RFC="Nuevo RFC 2",
                        TipoDocumento=4
                    )
                )
            )
        ]

        return ApiResponse(
            Success=True,
            Message="OK",
            Data=PaginationBase(Data=data),
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
                EstadoCode="cod1",
                EstadoNombre="Estado 1",
                PaisCode="MX",
                TipoMovimiento="Alta",
                Aviso="Aviso 1",
                Email="mail1@correo.com",
                FechaAviso="2025-01-07T00:00:00",
                FechaMovimiento="2025-01-07T00:00:00",
                Telefono="+52 123456",
                Nombre="Nombre 1",
                Puesto="Puesto 1",
            ),
        ),
        HistoricoResponse(
            Status="Modificado",
            Usuario="Usuario 2",
            Fecha="2025-01-07T00:00:00",
            Data=EnlaceOperativoResponse(
                ID=2,
                CaseNumber=2,
                EstadoCode="cod2",
                EstadoNombre="Estado 2",
                PaisCode="US",
                TipoMovimiento="Baja",
                Aviso="Aviso 2",
                Email="mail2@correo.com",
                FechaAviso="2025-01-07T00:00:00",
                FechaMovimiento="2025-01-07T00:00:00",
                Telefono="+1 123456",
                Nombre="Nombre 2",
                Puesto="Puesto 2",
            ),
        ),
    ]

    try:
        return ApiResponse(
            Success=True,
            Message="OK",
            Data=PaginationBase(
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


@app.post("/saveEnlaceOperativo")
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
