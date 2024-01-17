from django.urls import path

from eshop_contact_us.views import contact_page

app_name = "contact"
urlpatterns = [
    path('contact-us', contact_page, name="contact_us")
]
