from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, StockMovement

@receiver(post_save, sender=Product)
def update_low_stock_on_product_save(sender, instance, **kwargs):
    instance.low_stock = (instance.quantity <= instance.reorder_level)
    Product.objects.filter(pk=instance.pk).update(low_stock=instance.low_stock)

@receiver(post_save, sender=StockMovement)
def apply_stock_movement(sender, instance, created, **kwargs):
    if created:
        instance.apply()