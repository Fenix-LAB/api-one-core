from sqlalchemy import Column, Integer, String, Boolean, Float

from . import Base

class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    operations_value = Column(Float, nullable=True)
    positive_opinion = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "operations_value": self.operations_value,
            "positive_opinion": self.positive_opinion
        }
