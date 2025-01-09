from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_legal_uso_model import DatosEmpresaLegalUsoModel

class LegalUsoResponse(BaseModel):
    ID: int = Field(..., description="ID")
    CaseNumber: int = Field(..., description="Case number")
    DomicilioAcreditacion: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio acreditacion")
    DomicilioNuevo: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio nuevo")