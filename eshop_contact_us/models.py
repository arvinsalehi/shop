from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return self.subject

