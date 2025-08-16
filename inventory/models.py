from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Added
    updated_at = models.DateTimeField(auto_now=True)      # ✅ Added

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)  # Added
    email = models.EmailField()                # Added
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)   # ✅ Added
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # ✅ Added
    quantity = models.PositiveIntegerField(default=0)  # ✅ Added
    stock = models.PositiveIntegerField(default=0)     # optional
    low_stock = models.BooleanField(default=False)     # ✅ Added

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=50, choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')])
    quantity = models.PositiveIntegerField()
    note = models.TextField(blank=True, null=True)   # ✅ Added
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Added

    def __str__(self):
        return f"{self.movement_type} - {self.product.name}"