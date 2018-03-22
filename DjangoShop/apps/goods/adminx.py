import xadmin
from goods.models import Banner
from goods.models import Goods
from goods.models import GoodsCategory
from goods.models import GoodsCategoryBrand
from goods.models import GoodsImage


class GoodsCategoryAdmin(object):
    search_fields = ('name',)
    list_filter = ('category_type',)


class GoodsCategoryBrandAdmin(object):
    pass


class GoodsAdmin(object):
    search_fields = ('name',)
    ordering = ('name', 'sold_num')


class GoodsImageAdmin(object):
    pass


class BannerAdmin(object):
    pass


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
