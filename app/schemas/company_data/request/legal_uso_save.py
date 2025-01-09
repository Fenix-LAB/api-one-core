from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_legal_uso_model import DatosEmpresaLegalUsoModel

class LegalUsoSaveRequest(BaseModel):
    ID: int = Field(..., description="ID")
    DomicilioAcreditacion: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio acreditacion")
    DomicilioNuevo: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio nuevo")