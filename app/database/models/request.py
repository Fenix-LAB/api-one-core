from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String, nullable=False)
    status = Column(String, nullable=False)  # Ejemplo: "Pending Review"
    review_date = Column(DateTime, nullable=True)
    case_number = Column(Integer, nullable=False)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    requirement = relationship("Requirement")

    def to_dict(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "status": self.status,
            "review_date": self.review_date,
            "case_number": self.case_number,
            "requirement_id": self.requirement_id
        }
