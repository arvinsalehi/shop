import itertools
import time

from django.db.models import Q
from django.db import models
from PIL import Image
from eshop_products_category.models import ProductCategory
from eshop_tag.models import Tag
import os


def gen_file_ext(filepath):
    file = os.path.basename(filepath)
    name, ext = os.path.splitext(file)
    return name, ext


def file_upload_name(instance, filename):
    name, ext = gen_file_ext(filename)
    upload_name = f"{instance.id}-{instance.title}.{ext}"
    return f"products/{upload_name}"


def file_upload_gallery_image(instance, filename):
    name, ext = gen_file_ext(filename)
    upload_name = f"{instance.id}-{instance.title}.{ext}"
    return f"products/galleries/{upload_name}"


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ProductManager(models.Manager):
    def get_active(self):
        return self.get_queryset().filter(active=True)

    def get_by_product_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1000)
    image = models.ImageField(upload_to=file_upload_name, blank=False, null=True)
    active = models.BooleanField(default=True)
    visit = models.IntegerField(default=0, editable=False)
    dateTime = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(ProductCategory, blank=False)

    objects = ProductManager()

    def save(self, *args, **kwargs):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def __str__(self):
        return self.title


class Product_Image_Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=file_upload_gallery_image, blank=False, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
