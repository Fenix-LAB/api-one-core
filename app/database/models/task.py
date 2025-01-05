from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String, nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    risk_level = Column(String, nullable=False)  # Example: Low, Medium, High
    status = Column(String, nullable=False)
    user = relationship("User")

    def to_dict(self):
        return {
            "id": self.id,
            "area": self.area,
            "assigned_to": self.assigned_to,
            "risk_level": self.risk_level,
            "status": self.status,
            "user": self.user.to_dict()
        }
