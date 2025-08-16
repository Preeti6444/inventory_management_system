from django.contrib.auth.decorators import user_passes_test

def is_admin(user): return user.is_authenticated and user.role == 'ADMIN'
def is_staff_or_admin(user): return user.is_authenticated and user.role in ('ADMIN','STAFF')

admin_required = user_passes_test(is_admin)
staff_required = user_passes_test(is_staff_or_admin)