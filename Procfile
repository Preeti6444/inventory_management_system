release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn inventory_management_system.wsgi:application