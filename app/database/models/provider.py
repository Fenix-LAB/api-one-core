from sqlalchemy import Column, Integer, String, Boolean, Float

from . import Base

class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rfc = Column(String, nullable=False)
    value_operations = Column(Float, nullable=True)
    positive_opinion = Column(Boolean, default=False)
    virtual_operations = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rfc": self.rfc,
            "value_operations": self.value_operations,
            "positive_opinion": self.positive_opinion,
            "virtual_operations": self.virtual_operations
        }
