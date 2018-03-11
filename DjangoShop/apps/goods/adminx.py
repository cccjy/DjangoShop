import xadmin
from goods.models import Banner
from goods.models import Goods
from goods.models import GoodsCategory
from goods.models import GoodsCategoryBrand
from goods.models import GoodsImage


class GoodsCategoryAdmin(object):
    pass


class GoodsCategoryBrandAdmin(object):
    pass


class GoodsAdmin(object):
    pass


class GoodsImageAdmin(object):
    pass


class BannerAdmin(object):
    pass


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
