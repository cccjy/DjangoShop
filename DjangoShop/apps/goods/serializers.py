from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer2(serializers.ModelSerializer):
    """
        CategorySerializer2
    """

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
        CategorySerializer
    """
    sub_cat = CategorySerializer2(many=True)

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
