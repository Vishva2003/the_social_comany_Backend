# Generated by Django 5.1.1 on 2024-09-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_images_alter_product_offer_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='seller',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='sellers/'),
        ),
    ]
