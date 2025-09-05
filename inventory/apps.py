from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.contrib.auth import get_user_model


class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

