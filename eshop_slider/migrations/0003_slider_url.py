# Generated by Django 3.1.6 on 2021-02-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_slider', '0002_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
