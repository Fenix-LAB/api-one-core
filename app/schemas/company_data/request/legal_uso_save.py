from pydantic import BaseModel, Field
from app.schemas.models.datos_empresa_legal_uso import DatosEmpresaLegalUsoModel
from uuid import UUID
from datetime import datetime

class LegalUsoSaveRequest(BaseModel):
    id: UUID = Field(..., description="Id")
    status: int = Field(..., description="Status")
    esActual: bool = Field(..., description="Es actual")
    esAcreditacion: bool = Field(..., description="Es acreditacion")
    ratificarDomicilio: bool = Field(..., description="Ratificar domicilio")
    tipoDocumento: int = Field(..., description="Tipo documento")
    fechaInicioVigencia: datetime = Field(..., description="Fecha inicio vigencia")
    fechaVencimiento: datetime = Field(..., description="Fecha vencimiento")
    rfc: str = Field(..., description="RFC")    
    arrendador: str = Field(..., description="Arrendador")
    aviso: str = Field(..., description="Aviso")
    fechaAviso: datetime = Field(..., description="Fecha aviso")
    domicilio: DatosEmpresaLegalUsoModel = Field(..., description="Domicilio")
