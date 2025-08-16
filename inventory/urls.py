from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Product CRUD
    path('product/add/', views.product_add, name='product_add'),
    path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Category CRUD
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Supplier CRUD
    path('supplier/add/', views.supplier_add, name='supplier_add'),
    path('supplier/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
    path('supplier/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
]