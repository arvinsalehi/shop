from django.contrib import admin

from eshop_order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "is_paid"]
    list_filter = ['is_paid']
    list_editable = ["is_paid"]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["__str__", "owner_id", "product_id", "price"]
    search_fields = ["product__id"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
