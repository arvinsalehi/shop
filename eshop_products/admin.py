from django.contrib import admin
from .models import Product, Product_Image_Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "title", "price", "active", "dateTime"]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Image_Gallery)
