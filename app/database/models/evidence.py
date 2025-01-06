from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Evidence(Base):
    __tablename__ = "evidences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    requirement = relationship("Requirement", back_populates="evidences")

    def to_dict(self):
        return {
            "id": self.id,
            "file_name": self.file_name,
            "file_url": self.file_url,
            "file_size": self.file_size,
            "requirement_id": self.requirement_id,
            "requirement": self.requirement.to_dict(),
        }
