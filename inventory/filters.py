import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_qty = django_filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    max_qty = django_filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    low_stock = django_filters.BooleanFilter(field_name='low_stock')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category','low_stock','min_qty','max_qty','name']