from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject

from app.middleware.authentication import BaseData

from app.database.session import get_db_session

from app.schemas.generic_response import ApiResponse
from app.schemas.generic_list import ListResponse
from app.schemas.requirements.response import RequerementsObligationsResponse
from app.schemas.responsable.request import ResponsableRequest

from app.services.get_requirement_obligation import get_requerimiento_obligaciones
from app.services.role_checker import RoleChecker, get_current_user


app = APIRouter()
security = HTTPBearer()


@app.post("/requirements/get_obligations")
@inject
async def GetRequirementObligation(
    _: RoleChecker = Depends(RoleChecker(allowed_roles=["admin"])),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_data: BaseData = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
    ## DESCRIPTION
    ### Endpoint to get a count of requirements obligations.

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
        
        pending, near_due, findings = await get_requerimiento_obligaciones(db_session)

        response = RequerementsObligationsResponse(
            Pending=pending,
            NearDue=near_due,
            Findings=findings
        )

        return ApiResponse(
            Status="200",
            Message="Fetched requirements obligations successfully",
            Data=response,
            Token=user_data.token
        )
    
    except Exception as e:
        print(f'Error: {e}')
        return ApiResponse(
            Status="500",
            Message="Internal Server Error",
            Data=None,
            Token=user_data.token
        )

        
