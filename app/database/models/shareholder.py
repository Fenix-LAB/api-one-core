from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Shareholder(Base):
    __tablename__ = "shareholders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role_code = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="shareholders")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role_code": self.role_code,
            "company_id": self.company_id,
            "company": self.company.to_dict(),
        }
