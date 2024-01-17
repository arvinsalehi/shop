from django.db import models
from django.db.models.signals import pre_save, post_save
# from eshop_products.models import Product
from .utilities import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
