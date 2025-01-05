from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from . import Base

class Country(Base):
    __tablename__ = "countries"

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phone_code = Column(String, nullable=True)
    states = relationship("State", back_populates="country")

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "phone_code": self.phone_code,
            "states": [state.to_dict() for state in self.states]
        }
