from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    area = Column(String, nullable=False)  # Ejemplo: "finance", "legal"
    assigned = Column(Integer, default=0)
    completed = Column(Integer, default=0)
    risk_level = Column(String, nullable=False)  # Ejemplo: "low", "medium", "high"
    user = relationship("User", back_populates="tasks")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "area": self.area,
            "assigned": self.assigned,
            "completed": self.completed,
            "risk_level": self.risk_level,
            "user": self.user.to_dict()
        }
