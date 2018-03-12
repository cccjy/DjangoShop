from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GoodsSerializer
from .models import Goods


class GoodsListView(APIView):
    """
        List all goods
    """

    def get(self, request, format=None):
        """
            get
        :param request:
        :param format:
        :return:
        """
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)

        return Response(goods_serializer.data)
