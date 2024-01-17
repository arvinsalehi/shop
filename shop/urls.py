from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page, header, footer, about_us

urlpatterns = [
    path('', home_page, name="Home"),
    path('', include('eshop_contact_us.urls', namespace="contact")),
    path('', include('eshop_order.urls', namespace="order")),
    path('about-us', about_us, name="About"),
    path('', include('eshop_account.urls', namespace="login_register")),
    path('', include('eshop_products.urls', namespace="products")),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
