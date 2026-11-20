
from enum import Enum


class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    EMPLEADO = "empleado"
    CLIENTE = "cliente"