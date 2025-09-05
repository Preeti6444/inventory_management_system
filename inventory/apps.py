from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.contrib.auth import get_user_model


class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

    def ready(self):
        # Remove signals import if not needed
        # import inventory.signals  

        try:
            User = get_user_model()
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="adminpassword"
                )
                print("✅ Superuser created: admin / adminpassword")
        except (OperationalError, ProgrammingError):
            # Database is not ready yet
            pass