from django.contrib import admin

from goods.models import GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage, Banner


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(GoodsCategoryBrand)
class GoodsCategoryBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(GoodsImage)
class GoodsImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass
