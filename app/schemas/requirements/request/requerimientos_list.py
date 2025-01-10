from pydantic import BaseModel, Field
from datetime import datetime
from app.schemas.enums.requerimmientos_section_option_code import RequerimientosSectionOptionCode

class RequerimientosListRequest(BaseModel):
    Code: RequerimientosSectionOptionCode = Field(..., description="Requerimientos section option code")
    DateIni: datetime = Field(..., description="Start date")
    DateEnd: datetime = Field(..., description="End date")