from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    fax = models.CharField(max_length=20)
    about_us = models.TextField()
    copy_right = models.CharField(max_length=400)

    def __str__(self):
        return self.title
