from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from feincms.admin.item_editor import ItemEditor

from plata.product.admin import ProductVariationInline,\
    ProductPriceInline, ProductImageInline
from plata.product.models import Product
from . import models


class ProductAdmin(ItemEditor):
    show_on_top = ('is_active', 'name', 'slug')
    inlines = [ProductVariationInline, ProductPriceInline, ProductImageInline]
    list_display = ('is_active', 'name', 'sku', 'ordering')
    list_display_links = ('name',)
    list_filter = ('is_active',)
    filter_horizontal = ('categories', 'option_groups')
    prepopulated_fields = {'slug': ('name',)}


admin.site.unregister(Product)
admin.site.register(models.CMSProduct, ProductAdmin)
