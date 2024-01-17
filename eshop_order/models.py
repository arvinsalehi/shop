from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.owner.get_full_name()

    def get_amount(self):
        total_amount = 0
        for details in self.orderdetail_set.all():
            total_amount += details.get_sum()
        return total_amount

    def get_absolute_url(self):
        return f"/request/{self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner_id = models.IntegerField(null=True)
    price = models.IntegerField()
    count = models.IntegerField()

    def get_sum(self):
        return self.price * self.count

    def __str__(self):
        return self.product.title
