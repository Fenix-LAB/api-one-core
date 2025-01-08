from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Tabla de roles
class Role(Base):
    """
    Representa los roles dentro del sistema, como administrador, usuario, etc.
    Cada rol puede estar asociado a múltiples usuarios.
    """
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    users = relationship("User", secondary="user_roles", back_populates="roles")

# Tabla de áreas
class Area(Base):
    """
    Define áreas específicas dentro de la organización, como recursos humanos o legal.
    Cada área puede tener múltiples responsables asignados.
    """
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    responsables = relationship("Responsable", back_populates="area")

# Tabla de usuarios
class User(Base):
    """
    Almacena información de los usuarios del sistema, incluyendo su nombre de usuario y contraseña.
    Cada usuario puede tener múltiples roles asignados.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    roles = relationship("Role", secondary="user_roles", back_populates="users")

# Tabla de relación muchos a muchos entre usuarios y roles
class UserRole(Base):
    """
    Define la relación entre usuarios y roles, permitiendo asignar múltiples roles a un usuario.
    """
    __tablename__ = "user_roles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)

# Tabla de requerimientos
class Requirement(Base):
    """
    Representa los requerimientos asociados a los usuarios o procesos.
    Incluye fechas importantes y si el requerimiento es crítico.
    """
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_vencimiento = Column(DateTime, nullable=True)
    comentarios = Column(String, nullable=True)
    is_aprobado = Column(Boolean, default=False)
    es_critico = Column(Boolean, default=False)
    fecha_envio = Column(DateTime, nullable=True)
    responsables = relationship("Responsable", secondary="requirement_responsibles", back_populates="requirements")

# Tabla de responsables
class Responsable(Base):
    """
    Define a los responsables asociados con diferentes áreas y requerimientos.
    """
    __tablename__ = "responsables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    area_id = Column(Integer, ForeignKey("areas.id"))
    area = relationship("Area", back_populates="responsables")
    requirements = relationship("Requirement", secondary="requirement_responsibles", back_populates="responsables")

# Tabla de relación muchos a muchos entre requerimientos y responsables
class RequirementResponsible(Base):
    """
    Relación entre los requerimientos y los responsables asignados a estos.
    """
    __tablename__ = "requirement_responsibles"

    requirement_id = Column(Integer, ForeignKey("requirements.id"), primary_key=True)
    responsable_id = Column(Integer, ForeignKey("responsables.id"), primary_key=True)

# Tabla de evidencias de requerimientos
class RequirementEvidence(Base):
    """
    Almacena las evidencias asociadas a los requerimientos, incluyendo elementos relacionados y comentarios.
    """
    __tablename__ = "requirement_evidences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requirement_id = Column(Integer, ForeignKey("requirements.id"), nullable=False)
    elemento = Column(String, nullable=False)
    case_number = Column(Integer, nullable=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_vencimiento = Column(DateTime, nullable=True)
    proximo_vencer = Column(Boolean, default=False)
    ubicacion = Column(String, nullable=True)
    comentarios = Column(String, nullable=True)
    hallazgo_comentarios = Column(String, nullable=True)
    hallazgo_recomendaciones = Column(String, nullable=True)
    archivos = relationship("Document")

# Tabla de direcciones
class Address(Base):
    """
    Contiene la información de direcciones asociadas a entidades como empresas o usuarios.
    """
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pais_code = Column(String, ForeignKey("countries.code"), nullable=False)
    estado_code = Column(String, nullable=False)
    estado_name = Column(String, nullable=False)
    municipio = Column(String, nullable=True)
    localidad = Column(String, nullable=True)
    colonia = Column(String, nullable=True)
    calle = Column(String, nullable=True)
    numero_exterior = Column(String, nullable=True)
    numero_interior = Column(String, nullable=True)
    cp = Column(String, nullable=True)

# Tabla de movimientos
class Movement(Base):
    """
    Almacena los movimientos realizados por entidades como empresas o usuarios.
    """
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_movimiento = Column(DateTime, nullable=True)
    aviso = Column(String, nullable=True)
    fecha_aviso = Column(DateTime, nullable=True)

# Tabla de documentos
class Document(Base):
    """
    Representa documentos subidos al sistema, incluyendo información como tamaño y extensión.
    """
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=True)
    file_extension = Column(String, nullable=True)
    url = Column(String, nullable=True)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    requirement = relationship("Requirement", back_populates="documents")

# Tabla de hallazgos
class Finding(Base):
    """
    Almacena los hallazgos relacionados con los requerimientos, como comentarios y recomendaciones.
    """
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    comentarios = Column(String, nullable=True)
    recomendaciones = Column(String, nullable=True)

# Tabla de países
class Country(Base):
    """
    Contiene información sobre países, como el código y el nombre.
    Relacionado con direcciones.
    """
    __tablename__ = "countries"

    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phone_code = Column(String, nullable=True)
    states = relationship("Address", back_populates="country")

# Tabla de empresas
class Company(Base):
    """
    Almacena información sobre empresas, incluyendo datos fiscales y asociados.
    """
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    rfc = Column(String, nullable=False)
    case_number = Column(Integer, nullable=True)
    folio = Column(String, nullable=True)
    deed_date = Column(DateTime, nullable=True)
    fedatario = Column(String, nullable=True)
    notary = Column(String, nullable=True)
    fecha_movimiento = Column(DateTime, nullable=True)
    pais_code = Column(String, ForeignKey("countries.code"))
    shareholders = relationship("CompanyShareholder", back_populates="company")

# Tabla de socios y accionistas
class CompanyShareholder(Base):
    """
    Representa a los socios y accionistas de las empresas, con detalles como RFC y movimientos.
    """
    __tablename__ = "company_shareholders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    nombre = Column(String, nullable=False)
    rfc = Column(String, nullable=False)
    caracter_code = Column(String, nullable=True)
    movimiento_id = Column(Integer, ForeignKey("movements.id"))
    movimiento = relationship("Movement")
    company = relationship("Company", back_populates="shareholders")

# Tabla de notificaciones
class Notification(Base):
    """
    Define las notificaciones enviadas dentro del sistema, incluyendo su estado y descripción.
    """
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    state = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    is_error = Column(Boolean, default=False)

# Tabla de expedientes CIVA
class ExpedienteCiva(Base):
    """
    Almacena expedientes del sistema, con información de actualizaciones y creación.
    """
    __tablename__ = "expedientes_civa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    actualizacion = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

# Tabla de históricos
class HistoricalRecord(Base):
    """
    Registra cambios históricos realizados en entidades del sistema.
    """
    __tablename__ = "historical_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_type = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=False)
    change_date = Column(DateTime, default=datetime.utcnow)
    change_description = Column(String, nullable=True)

# Tabla de solicitudes
class Solicitation(Base):
    """
    Almacena información sobre solicitudes realizadas en el sistema, con detalles como cliente y caso.
    """
    __tablename__ = "solicitations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    elemento = Column(String, nullable=False)
    case_number = Column(Integer, nullable=False)
    cliente = Column(String, nullable=False)
    fecha_revision = Column(DateTime, nullable=True)
    comentarios = Column(String, nullable=True)
    responsables = relationship("Responsable")
