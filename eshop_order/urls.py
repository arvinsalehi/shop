from django.urls import path

from eshop_order.views import user_order, user_basket, send_request, verify, remove_order

app_name = "order"

urlpatterns = [
    path('new-order', user_order, name='new-order'),
    path('basket', user_basket, name='basket'),
    path('remove-order/<detail_id>', remove_order),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
]
