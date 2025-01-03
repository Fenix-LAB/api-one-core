from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))  # Relación con Requirement
    requirement = relationship("Requirement", back_populates="findings")

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "requirement_id": self.requirement_id
        }
