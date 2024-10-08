# Generated by Django 5.1.1 on 2024-09-11 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='review_images/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='seller_logos/')),
                ('rating', models.FloatField()),
                ('warranty_offer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='product_images/')),
                ('description', models.TextField()),
                ('original_price', models.FloatField()),
                ('offer_price', models.FloatField()),
                ('reviews', models.ManyToManyField(to='products.review')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.seller')),
            ],
        ),
    ]
