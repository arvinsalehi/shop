# Generated by Django 3.1.6 on 2021-02-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]