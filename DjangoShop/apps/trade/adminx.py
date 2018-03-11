import xadmin
from trade.models import ShoppingCart
from trade.models import OrderInfo
from trade.models import OrderGoods


class ShoppingCartAdmin(object):
    pass


class OrderInfoAdmin(object):
    pass


class OrderGoodsAdmin(object):
    pass


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
