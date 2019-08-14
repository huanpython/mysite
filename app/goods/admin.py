from django.contrib import admin

# Register your models here.
from app.goods.models import GoodsCategory, GoodsCategoryBrand, Goods, Banner, IndexAd, HotSearchWords


class GoodsAdmin(admin.ModelAdmin):
    #显示的列
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "is_new", "is_hot", "add_time"]


class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type", "parent_category", "add_time"]


# class GoodsBrandAdmin(admin.ModelAdmin):
#     list_display = ["category", "image", "name", "desc"]


class BannerGoodsAdmin(admin.ModelAdmin):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(admin.ModelAdmin):
    list_display = ["keywords", "index", "add_time"]

class IndexAdAdmin(admin.ModelAdmin):
    list_display = ["category", "goods"]


admin.site.site_header = "生鲜项目后台管理"

admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Goods, GoodsAdmin)

admin.site.register(Banner, BannerGoodsAdmin)
admin.site.register(IndexAd, IndexAdAdmin)
admin.site.register(HotSearchWords, HotSearchAdmin)
