from django.contrib import admin
from eshop_products.models import Product
from eshop_tag.models import Tag


class ProductsInline(admin.TabularInline):
    model = Product.tag.through


class TagAdmin(admin.ModelAdmin):
    inlines = [
        ProductsInline,
    ]


admin.site.register(Tag, TagAdmin)
