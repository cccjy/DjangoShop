import django_filters
from django_filters.rest_framework import FilterSet

from goods.models import Goods


class GoodsFilter(FilterSet):
    """
        商品过滤类
    """
    price_min = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']
