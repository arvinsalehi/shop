from django.shortcuts import render

from eshop_products.models import Product, my_grouper
from eshop_slider.models import Slider
from eshop_settings.models import SiteSetting


def header(request, *args, **kwargs):
    context = {}
    return render(request, "shared/Header.html", context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'site_settings': site_setting
    }
    return render(request, "shared/Footer.html", context)


def home_page(request):
    slider = Slider.objects.all()
    most_visit_product = Product.objects.order_by("visit").all()[:8]
    latest_product = Product.objects.order_by("-id").all()[:8]
    context = {
        "title": "home_page",
        "slider": slider,
        "most_visit_product": my_grouper(4, most_visit_product),
        "latest_product": my_grouper(4, latest_product),
    }
    return render(request, "home_page.html", context)


def about_us(request):
    context = {
        "title": "about_us"
    }
    return render(request, "about_us.html", context)
