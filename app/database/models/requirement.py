from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    section_code = Column(String, nullable=False)
    description = Column(String, nullable=False)
    critical = Column(Boolean, default=False)
    status = Column(String, nullable=False)
    due_date = Column(DateTime, nullable=True)
    evidences = relationship("Evidence", back_populates="requirement")

    def to_dict(self):
        return {
            "id": self.id,
            "section_code": self.section_code,
            "description": self.description,
            "critical": self.critical,
            "status": self.status,
            "due_date": self.due_date,
            "evidences": [evidence.to_dict() for evidence in self.evidences]
        }
