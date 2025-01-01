from sqlalchemy import Column, Integer, String

from . import Base

class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name
        }
