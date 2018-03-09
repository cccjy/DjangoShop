from django.contrib import admin

from trade.models import ShoppingCart, OrderInfo, OrderGoods


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderGoods)
class OrderGoodsAdmin(admin.ModelAdmin):
    pass
