from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from eshop_order.forms import UserOrderForm
from .models import Product, Product_Image_Gallery, my_grouper
from eshop_products_category.models import ProductCategory


class ProductList(ListView):
    template_name = "products/productList.html"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active()


class ProductListByCategory(ListView):
    template_name = "products/productList.html"
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه ی مورد نظر یافت نشد")
        return Product.objects.get_by_product_category(category_name)


def product_detail(request, *args, **kwargs):
    product_id = kwargs['product_id']
    print(product_id)
    user_order_form = UserOrderForm(request.POST or None, initial={'product_id': product_id})
    product: Product = Product.objects.get_by_id(product_id)
    if product is None or not product.active:
        raise Http404
    product.visit += 1
    product.save()
    product_galleries = Product_Image_Gallery.objects.filter(product_id=product_id)
    grouped_galleries = list(my_grouper(3, product_galleries))
    related_product = Product.objects.get_queryset().filter(categories__product=product).distinct()
    grouped_related_product = my_grouper(3, related_product)
    context = {
        "product": product,
        "galleries": grouped_galleries,
        "related_products": grouped_related_product,
        "user_order_form": user_order_form,
    }
    return render(request, 'products/product_detail.html', context)


class SearchProduct(ListView):
    template_name = "products/productList.html"
    paginate_by = 6

    def get_queryset(self):
        request = self.request.GET
        qs = request.get("q")
        if qs is not None:
            return Product.objects.search(qs)
        return Product.objects.all()


def product_category_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'products/components/product_category_partial.html', context)
