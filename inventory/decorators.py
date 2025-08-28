from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", "") == "admin":
            return view_func(request, *args, **kwargs)
        return redirect("no_permission")
    return wrapper

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", "") in ("staff", "admin"):
            return view_func(request, *args, **kwargs)  # allow admin to see staff pages too
        return redirect("no_permission")
    return wrapper

    return redirect("some_existing_view_name")

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
            # user does not have permission
            return render(request, 'inventory/no_permission.html')
        return wrapper_func
    return decorator