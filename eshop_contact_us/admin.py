from django.contrib import admin

# Register your models here.
from eshop_contact_us.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "is_read"]
    list_filter = ['is_read']
    search_fields = ["subject", "full_name"]
    list_editable = ["is_read"]


admin.site.register(ContactUs, ContactUsAdmin)
