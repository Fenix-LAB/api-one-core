from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_enlace_operativo_model import DatosEmpresaEnlaceOperativoModel

class EnlaceOperativoSaveRequest(DatosEmpresaEnlaceOperativoModel):
    ID: int = Field(..., description="ID")