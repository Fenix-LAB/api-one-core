from sqlalchemy import Column, Integer, String

from . import Base

class Responsable(Base):
    __tablename__ = "responsables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    area_code = Column(String, nullable=False)  # Ejemplo: "admin", "finance", etc.

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "area_code": self.area_code
        }
