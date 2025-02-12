from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_legal_uso import DatosEmpresaLegalUsoModel

class LegalUsoResponse(BaseModel):
    id: int = Field(..., description="ID")
    caseNumber: int = Field(..., description="Case number")
    domicilioAcreditacion: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio acreditacion")
    domicilioNuevo: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio nuevo")