from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    section_code = Column(String, nullable=False)  # Ejemplo: "Personal", "Fiscal"
    elements = Column(String, nullable=False)
    expiration = Column(String, nullable=True)  # Ejemplo: "30 días"
    is_critical = Column(Boolean, default=False)
    verification_status = Column(String, nullable=False)  # Ejemplo: "Pending", "Approved"
    sent_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=True)  # Nueva columna para fecha de vencimiento
    responsible_id = Column(Integer, ForeignKey("responsables.id"))
    findings = relationship("Finding", back_populates="requirement")

    def to_dict(self):
        return {
            "id": self.id,
            "section_code": self.section_code,
            "elements": self.elements,
            "expiration": self.expiration,
            "is_critical": self.is_critical,
            "verification_status": self.verification_status,
            "sent_date": self.sent_date,
            "due_date": self.due_date,
            "responsible_id": self.responsible_id
        }
