# Generated by Django 3.1.6 on 2021-02-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0001_initial'),
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='eshop_products_category.ProductCategory'),
        ),
    ]