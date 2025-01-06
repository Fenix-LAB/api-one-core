from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
    Registering Tables in the database
"""

from .user import User
from .role import Role
from .responsable import Responsable
from .notification import Notification
from .task import Task
from .company import Company
from .shareholder import Shareholder
from .provider import Provider
from .country import Country
from .requirement import Requirement
from .evidence import Evidence
from .finding import Finding
from .request import Request
from .state import State
from .client import Client
