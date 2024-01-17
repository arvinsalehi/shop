from django.urls import path
from .views import ProductList, product_detail, SearchProduct, ProductListByCategory, product_category_partial

app_name = "products"

urlpatterns = [
    path('products', ProductList.as_view(), name='products'),
    path('products/category/<category_name>', ProductListByCategory.as_view()),
    path('products/<product_id>/<product_name>', product_detail, name='product_detail'),
    path('products/<search>', SearchProduct.as_view()),
    path('product_category_partial', product_category_partial, name="product_category_partial"),
]
