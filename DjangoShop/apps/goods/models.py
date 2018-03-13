from django.db import models
from django.utils import timezone

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
        商品类别
    """

    name = models.CharField(default='', max_length=30, verbose_name='名字')
    code = models.CharField(default='', max_length=30, verbose_name='类别code')
    desc = models.CharField(default='', null=True, blank=True, max_length=30, verbose_name='描述')
    category_type_choices = (
        (1, '1'),
        (2, '1'),
        (3, '1'),
    )
    category_type = models.IntegerField(choices=category_type_choices, verbose_name='添加时间')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name='父类别',
                               related_name='sub_cat', on_delete=models.DO_NOTHING)
    is_tab = models.BooleanField(default=False, verbose_name='是否导航')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
        品牌名
    """
    name = models.CharField(default='', max_length=30, verbose_name='名字')
    desc = models.TextField(default='', max_length=30, verbose_name='描述')
    image = models.ImageField(max_length=200, upload_to='brand/images')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '品牌名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
        商品
    """
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类目', on_delete=models.DO_NOTHING)
    goods_sn = models.CharField(max_length=50, default='', verbose_name='商品唯一货号')
    name = models.CharField(max_length=100, verbose_name='商品名')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    sold_nums = models.IntegerField(default=0, verbose_name='商品销售量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    goods_nums = models.IntegerField(default=0, verbose_name='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简短描述')
    goods_desc = UEditorField(verbose_name='内容', imagePath='goods/images/', width=1000, height=300,
                              filePath='goods/files/', default='')
    ship_free = models.BooleanField(default=True, verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')
    is_new = models.BooleanField(default=False, verbose_name='是否新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否热销')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')
    is_del = models.BooleanField(default=False)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def remove(self):
        self.is_del = True
        self.save()


class GoodsImage(models.Model):
    """
        商品轮播图
    """

    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='', verbose_name='图片', null=True, blank=True)
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
        轮播商品
    """
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='banner', verbose_name='轮播图片')
    index = models.IntegerField(default=0, verbose_name='轮播顺序')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
