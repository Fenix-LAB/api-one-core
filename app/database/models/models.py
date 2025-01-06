from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Tabla de usuarios
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")
    tasks = relationship("Task", back_populates="user")


# Tabla de roles
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    users = relationship("User", back_populates="role")


# Tabla de responsables
class Responsable(Base):
    __tablename__ = "responsables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    area_code = Column(String, nullable=False)  # Ejemplo: "admin", "finance", etc.


# Tabla de notificaciones
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False)  # Ejemplo: "approved", "pending", etc.
    created_at = Column(DateTime, nullable=False)
    is_error = Column(Boolean, default=False)


# Tabla de tareas
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    area = Column(String, nullable=False)  # Ejemplo: "finance", "legal"
    assigned = Column(Integer, default=0)
    completed = Column(Integer, default=0)
    risk_level = Column(String, nullable=False)  # Ejemplo: "low", "medium", "high"
    user = relationship("User", back_populates="tasks")


# Tabla de empresas
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rfc = Column(String, nullable=False, unique=True)
    case_number = Column(Integer, nullable=True)
    creation_date = Column(DateTime, nullable=False)
    shareholders = relationship("Shareholder", back_populates="company")


# Tabla de socios y accionistas
class Shareholder(Base):
    __tablename__ = "shareholders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
    role = Column(String, nullable=False)  # Ejemplo: "shareholder", "partner"
    is_company = Column(Boolean, default=False)
    company = relationship("Company", back_populates="shareholders")


# Tabla de proveedores
class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    operations_value = Column(Float, nullable=True)
    positive_opinion = Column(Boolean, default=False)


# Tabla de países
class Country(Base):
    __tablename__ = "countries"

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phone_code = Column(String, nullable=True)


# Tabla de requerimientos
class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    section_code = Column(String, nullable=False)  # Ejemplo: "Personal", "Fiscal"
    elements = Column(String, nullable=False)
    expiration = Column(String, nullable=True)  # Ejemplo: "30 días"
    is_critical = Column(Boolean, default=False)
    verification_status = Column(String, nullable=False)  # Ejemplo: "Pending", "Approved"
    sent_date = Column(DateTime, nullable=False)
    responsible_id = Column(Integer, ForeignKey("responsables.id"))


# Tabla de evidencias
class Evidence(Base):
    __tablename__ = "evidences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    file_name = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    file_extension = Column(String, nullable=False)
    requirement = relationship("Requirement")


# Tabla de hallazgos
class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)


# Tabla de solicitudes
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String, nullable=False)
    status = Column(String, nullable=False)  # Ejemplo: "Pending Review"
    review_date = Column(DateTime, nullable=True)
    case_number = Column(Integer, nullable=False)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    requirement = relationship("Requirement")
