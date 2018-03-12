from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    """
        CategorySerializer
    """

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    """
        GoodsSerializer
    """
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
