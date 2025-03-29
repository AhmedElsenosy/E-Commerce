import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name='name' , lookup_expr='icontains')
    MinPrice = django_filters.NumberFilter(field_name='price' or 0 , lookup_expr='gte')
    MaxPrice = django_filters.NumberFilter(field_name='price' or 100000 , lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('category', 'brand' , 'keyword' , 'MinPrice' , 'MaxPrice')