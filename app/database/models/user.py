from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


# Tabla de usuarios
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role_id": self.role_id,
            "role": self.role.to_dict(),
        }
