from django.urls import path
from . import views

urlpatterns = [
    # Home / Dashboard
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Categories
    path("categories/", views.category_list, name="category_list"),       # public
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:pk>/edit/", views.category_update, name="category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),

    # Suppliers
    path("suppliers/", views.supplier_list, name="supplier_list"),        # public
    path("suppliers/create/", views.supplier_create, name="supplier_create"),
    path("suppliers/<int:pk>/edit/", views.supplier_update, name="supplier_update"),
    path("suppliers/<int:pk>/delete/", views.supplier_delete, name="supplier_delete"),

    # Products
    path("products/", views.product_list, name="product_list"),           # public
    path("products/create/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_update, name="product_update"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),

    # Restricted example
    path("restricted/", views.restricted_view, name="restricted_view"),
    path("no-permission/", views.no_permission_view, name="no_permission"),
]