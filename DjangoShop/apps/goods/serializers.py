from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    """
        GoodsSerializer
    """
    name = serializers.CharField(required=True, max_length=100)
    click_nums = serializers.IntegerField(default=0)
