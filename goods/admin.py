from django.contrib import admin

# Register your models here.
from goods.models import GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage, Banner, IndexAd, HotSearchWords


admin.site.site_header = "生鲜项目后台管理"

admin.site.register(GoodsCategory)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(Banner)
admin.site.register(IndexAd)
admin.site.register(HotSearchWords)
