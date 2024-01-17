import os

from django.db import models

from eshop_products.models import Product


def gen_file_ext(filepath):
    file = os.path.basename(filepath)
    name, ext = os.path.splitext(file)
    return name, ext


def file_upload_name(instance, filename):
    name, ext = gen_file_ext(filename)
    upload_name = f"{instance.id}-{instance.title}.{ext}"
    return f"products/{upload_name}"


class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField()
    url = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to=file_upload_name, blank=False, null=True)

    def __str__(self):
        return self.title
