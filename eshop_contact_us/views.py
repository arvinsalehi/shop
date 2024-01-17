from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs
from eshop_settings.models import SiteSetting


# Create your views here.
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get("full_name")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        text = contact_form.cleaned_data.get("text")
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        contact_form = ContactForm()
    site_settings = SiteSetting.objects.first()
    context = {
        "title": "contact-us",
        "contact_form": contact_form,
        "site_settings": site_settings,
    }

    return render(request, 'contact-us/contact_us.html', context)
