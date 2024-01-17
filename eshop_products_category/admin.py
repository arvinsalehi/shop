from django.contrib import admin
from eshop_products_category.models import ProductCategory
from eshop_products.models import Product


class ProductInline(admin.TabularInline):
    model = Product.categories.through


class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]


admin.site.register(ProductCategory, ProductCategoryAdmin)
