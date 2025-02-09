from pydantic import BaseModel, Field
from datetime import datetime
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class RequerimientosListRequest(BaseModel):
    code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    dateIni: datetime = Field(..., description="Start date")
    dateEnd: datetime = Field(..., description="End date")