from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Supplier, Product
from .forms import CategoryForm, SupplierForm, ProductForm
from .decorators import admin_required, staff_required  # <- move your decorators to inventory/decorators.py
from .decorators import allowed_users

@admin_required
def category_list(request):
    qs = Category.objects.all().order_by("name")
    return render(request, "inventory/category_list.html", {"categories": qs})

@admin_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Category created.")
        return redirect("category_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Create Category"})

@admin_required
def category_update(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Category updated.")
        return redirect("category_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Edit Category"})

@admin_required
def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Category deleted.")
        return redirect("category_list")
    return render(request, "inventory/confirm_delete.html", {"object": obj, "title": "Delete Category"})

@admin_required
def supplier_list(request):
    qs = Supplier.objects.all().order_by("name")
    return render(request, "inventory/supplier_list.html", {"suppliers": qs})

@admin_required
def supplier_create(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Supplier created.")
        return redirect("supplier_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Create Supplier"})

@admin_required
def supplier_update(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Supplier updated.")
        return redirect("supplier_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Edit Supplier"})

@admin_required
def supplier_delete(request, pk):
    obj = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Supplier deleted.")
        return redirect("supplier_list")
    return render(request, "inventory/confirm_delete.html", {"object": obj, "title": "Delete Supplier"})

@staff_required
def product_list(request):
    qs = Product.objects.select_related("category", "supplier").order_by("name")
    low = qs.filter(stock__lte=models.F("low_stock_threshold"))
    return render(request, "inventory/product_list.html", {"products": qs, "low_products": low})

@admin_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user
        obj.save()
        messages.success(request, "Product created.")
        return redirect("product_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Create Product"})

@admin_required
def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Product updated.")
        return redirect("product_list")
    return render(request, "inventory/form.html", {"form": form, "title": "Edit Product"})

@admin_required
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Product deleted.")
        return redirect("product_list")
    return render(request, "inventory/confirm_delete.html", {"object": obj, "title": "Delete Product"})

@login_required
@permission_required('inventory.view_item', raise_exception=True)
def restricted_view(request):
    return render(request, 'inventory/restricted_page.html')

def no_permission_view(request):
    return render(request, 'inventory/no_permission.html')

@allowed_users(allowed_roles=['Admin'])
def dashboard(request):
    # only admins can access
    return render(request, 'inventory/dashboard.html')

def some_protected_view(request):
    if not request.user.has_perm('inventory.can_add_product'):  # Example condition
        return redirect('no_permission') 