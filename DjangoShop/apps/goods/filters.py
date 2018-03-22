import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet

from goods.models import Goods


class GoodsFilter(FilterSet):
    """
        商品过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        """
            查询id下所有商品
        """
        queryset = queryset.filter(
            Q(category_id=value) |
            Q(category__parent_id=value) |
            Q(category__parent__parent_id=value)
        )

        return queryset

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
