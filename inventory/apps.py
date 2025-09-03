from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.utils import OperationalError, ProgrammingError

class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

    def ready(self):
        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="adminpassword"
                )
                print("✅ Superuser created: admin / adminpassword")
        except (OperationalError, ProgrammingError):
            # Database not ready yet, skip
            pass