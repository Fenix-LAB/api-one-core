from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Evidence(Base):
    __tablename__ = "evidences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    file_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    file_extension = Column(String, nullable=False)
    requirement = relationship("Requirement")

    def to_dict(self):
        return {
            "id": self.id,
            "requirement_id": self.requirement_id,
            "file_name": self.file_name,
            "file_url": self.file_url,
            "file_size": self.file_size,
            "file_extension": self.file_extension
        }
