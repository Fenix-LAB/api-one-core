from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Shareholder(Base):
    __tablename__ = "shareholders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
    role = Column(String, nullable=False)  # Ejemplo: "shareholder", "partner"
    is_company = Column(Boolean, default=False)
    company = relationship("Company", back_populates="shareholders")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "company_id": self.company_id,
            "role": self.role,
            "is_company": self.is_company
        }
