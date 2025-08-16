from django.contrib import admin
from .models import Category, Supplier, Product, StockMovement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone', 'address')
    search_fields = ('name', 'contact_email')
    def contact_email(self, obj):
        return obj.email

    def phone(self, obj):
        return obj.contact
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'supplier', 'quantity', 'low_stock', 'selling_price')
    list_filter = ('category', 'supplier', 'low_stock')
    search_fields = ('sku', 'name')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'note', 'created_at')
    list_filter = ('movement_type', 'created_at')