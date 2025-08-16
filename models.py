from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class User(AbstractUser):
    role = models.CharField(max_length=50, blank=True, null=True)

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Supplier model
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)  # Add this
    email = models.EmailField()  # Add this
    address = models.TextField()

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=5)  # NEW FIELD
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Stock Movement model
class StockMovement(models.Model):
    MOVEMENT_TYPE = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"