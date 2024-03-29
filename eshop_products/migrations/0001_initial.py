# Generated by Django 3.1.6 on 2021-02-20 15:46

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=1000, max_digits=15)),
                ('image', models.ImageField(null=True, upload_to=eshop_products.models.file_upload_name)),
                ('active', models.BooleanField(default=True)),
                ('tag', models.ManyToManyField(blank=True, to='eshop_tag.Tag')),
            ],
        ),
    ]
