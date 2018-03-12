from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .serializers import GoodsSerializer
from .models import Goods


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
        商品列表页
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
