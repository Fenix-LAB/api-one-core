from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from . import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rfc = Column(String, nullable=False, unique=True)
    case_number = Column(Integer, nullable=True)
    creation_date = Column(DateTime, nullable=False)
    shareholders = relationship("Shareholder", back_populates="company")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rfc": self.rfc,
            "case_number": self.case_number,
            "creation_date": self.creation_date,
            "shareholders": [shareholder.to_dict() for shareholder in self.shareholders]
        }
