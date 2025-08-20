from django.shortcuts import redirect

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